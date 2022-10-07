from blurNode import create_blur_group
import bpy
class somatomapNode(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Custom Somatomap Node"
    bl_idname = "NODE_BLUR"
    bl_space_type = 'NODE_EDITOR'
    bl_region_type = 'UI'
    bl_category = "Custom Blur"
    
    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.operator("")

def create_blur_group(context, operator, group_name):
    
    #enable use of nodes
    bpy.context.object.active_material.use_nodes = True
    
    #add a group
    blur_group = bpy.data.node_groups.new(group_name, 'ShaderNodeTree'):
        #create group for inputs
        #group_in  = blur_group.nodes.new('NodeGroupInput')
        #blur_group.inputs.new('NodeSocketFloat', 'Blur Amount')
        #blur_group.inputs.new('NodeSocketFloat', 'Blur Quality')
        
        #create group output
        #group_out = blur_group.nodes.new('NodeGroupOutput')
        #blur_group.outputs.new('NodeSocketColor', 'Color')
        
        #noise_texture = blur_group.nodes.new(type="ShaderNodeTexNoise", use_transform=True)
        #texture_coordinate = blur_group.nodes.new(type="ShaderNodeTexCoord", use_transform=True)
        
        #mixRGBadd = blur_group.nodes.new(type="ShaderNodeMixRGB", use_transform=True)
        
        #mixRGBsub = blur_group.nodes.new(type="ShaderNodeMixRGB", use_transform=True)

def execute(self, context):
    blur_group = create_blur_group(self, context, 'Blur Node')
    node_tree = context.object.active_materials.node_tree
    new_node = node_tree.nodes.new("ShaderNodeGroup")
    new_node.node_tree = bpy.data.node_groups[blur_group]