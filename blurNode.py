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
        #group in
    group_in  = blur_group.nodes.new('NodeGroupInput')
    group_in.location = (-400,0)
        #group out
    group_out = blur_group.nodes.new('NodeGroupOutput')
    group_out.location = (400,0)
    
        #outputs
    blur_group.inputs.new('NodeSocketFloat', 'Blur Amount')
    blur_group.inputs.new('NodeSocketFloat', 'Blur Quality')
        #inputs
    blur_group.outputs.new('NodeSocketColor', 'Color')
            
    #add noise texture
    noise_texture = blur_group.nodes.new(type="ShaderNodeTexNoise")
    noise_texture.location = (-200,-150)
    #add texture coordinate
    texture_coordinate = blur_group.nodes.new(type="ShaderNodeTexCoord")
    texture_coordinate.location = (-200,150)
            
    #add mixRGB node 
    mixRGBadd = blur_group.nodes.new(type="ShaderNodeMixRGB")
    mixRGBadd.blend_type='ADD'
    mixRGBadd.inputs[0].default_value = 0.1
    mixRGBadd.location = (200,150)

    #add another mixRGB, this one will be subtract blend type
    mixRGBsub = blur_group.nodes.new(type="ShaderNodeMixRGB")
    mixRGBsub.blend_type='SUBTRACT'
    mixRGBsub.inputs[0].default_value = 1
    mixRGBsub.location = (75,-150)
            
    # Create links between nodes
    link = blur_group.links.new
   
    link(group_in.outputs[0], mixRGBadd.inputs[0])
    link(group_in.outputs[1], noise_texture.inputs[1])
    
    link(texture_coordinate.outputs[2], mixRGBadd.inputs[1])
    link(noise_texture.outputs[1], mixRGBsub.inputs[1])
    link(mixRGBsub.outputs[0], mixRGBadd.inputs[2])
    link(mixRGBadd.outputs[0], group_out.inputs[0])
            
    return blur_group


# Create a custom operator for the blur shader
class SHADER_OT_BLUR(bpy.types.Operator):
    bl_label = 'Blur Texture'
    bl_idname = 'shader.blur_ot'

    def execute(self, context):
        custom_node_name = "Blur Node"
        my_group = create_blur_group(self, context, custom_node_name)
        node_tree = context.object.active_material.node_tree
        new_node = node_tree.nodes.new("ShaderNodeGroup")
        new_node.node_tree = bpy.data.node_groups[my_group.name]
        
        return {'FINISHED'}


def register():
    bpy.utils.register_class(shaderPanel)
    bpy.utils.register_class(SHADER_OT_BLUR)


def unregister():
    bpy.utils.unregister_class(shaderPanel)
    bpy.utils.register_class(SHADER_OT_BLUR)


if __name__ == "__main__":
    register()
