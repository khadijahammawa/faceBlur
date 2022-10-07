import bpy

# Create a custom UI panel for shader library
class shaderPanel(bpy.types.Panel):
    bl_label = "Shader Library"
    bl_idname = "SHADER_PT"
    bl_space_type = 'NODE_EDITOR'
    bl_region_type = 'UI'
    bl_category = "Shader Library"

    def draw(self, context):
        layout = self.layout
        
        row = layout.row()
        row.label(text="Select Shader to be Addded")
        row.operator('shader.blur_ot')

def create_blur_group(context, operator, group_name):
    bpy.context.object.active_material.use_nodes = True
    
    #add a group
    blur_group = bpy.data.node_groups.new(group_name, 'ShaderNodeTree')
    #create group for inputs
    group_in  = blur_group.nodes.new('NodeGroupInput')
    blur_group.inputs.new('NodeSocketFloat', 'Blur Amount')
    blur_group.inputs.new('NodeSocketFloat', 'Blur Quality')
        
    #create group output
    group_out = blur_group.nodes.new('NodeGroupOutput')
    blur_group.outputs.new('NodeSocketColor', 'Color')
            
    #add noise texture
    noise_texture = blur_group.nodes.new(type="ShaderNodeTexNoise", use_transform=True)
    #add texture coordinate
    texture_coordinate = blur_group.nodes.new(type="ShaderNodeTexCoord", use_transform=True)
            
    #add mixRBG node 
    mixRGBadd = blur_group.nodes.new(type="ShaderNodeMixRGB", use_transform=True)
    bpy.data.materials["Material"].node_tree.nodes["Mix"].blend_type = 'ADD'
    bpy.data.materials["Material"].node_tree.nodes["Mix"].inputs[0].default_value = 0.1

    #add another mixRBG, this one will be subtract blend type
    mixRGBsub = blur_group.nodes.new(type="ShaderNodeMixRGB", use_transform=True)
    bpy.data.materials["Material"].node_tree.nodes["Mix.001"].blend_type = 'SUBTRACT'
    bpy.data.materials["Material"].node_tree.nodes["Mix.001"].inputs[0].default_value = 1
            
    # Create links between nodes
    link = blur_group.links.new

    #connects texture coordinate UV to mixRBG(add) Color 1
    link(texture_coordinate.outputs[2], mixRBGadd.inputs[1])
            
    #connects noise texture color output to mixRGB(sub) Color 1
    link(noise_texture.outputs[1], mixRBGsub.inputs[1])
            
    #connects mixRGB (sub) Color output to mixRGB(add) Color 2
    link(mixRGBsub.outputs[0], mixRBGadd.inputs[1])
            
    #connect group blur amount output to mixRBG(add) Fac
    link(group_in.outputs[0], mixRBGadd.inputs[0])
            
    #connect group blur quality output to mixRBG(add) Fac
    link(group_in.outputs[1], noise_texture.inputs[1])
            
    #connect mixRGB(add) to group output Color 
    link(mixRGBadd.outputs[0], group_out.inputs[0])
            
    return blur_group


# Create a custom operator for the blur shader
class SHADER_OT_BLUR(bpy.types.Operator):
    bl_label = 'Blur Textture'
    bl_idname = 'shader.blur_ot'

    def execute(self, context):
        custom_node_name = "Blur Node"
        my_group = create_test_group(self, context, custom_node_name)
        node_tree = context.object.active_material.node_tree
        new_node = node_tree.nodes.new("ShaderNodeGroup")
        new_node.node_tree = bpy.data.node_groups[my_group.name]


def register():
    bpy.utils.register_class(shaderPanel)
    bpy.utils.register_class(SHADER_OT_BLUR)


def unregister():
    bpy.utils.unregister_class(shaderPanel)
    bpy.utils.register_class(SHADER_OT_BLUR)


if __name__ == "__main__":
    register()
