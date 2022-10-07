import bpy

## CREATE PANEL FOR SHADER TAB ##
class somatomapNode(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Custom Somatomap Node"
    bl_idname = "NODE_BLUR"
    bl_space_type = 'NODE_EDITOR'
    bl_region_type = 'UI'
    bl_category = "New Tab"

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.operator("")

def create_blur_group(context, operator, group_name):


def register():
    bpy.utils.register_class(somatomapNode)


def unregister():
    bpy.utils.unregister_class(somatomapNode)


if __name__ == "__main__":
    register()
########################################
###
########################################


# noise texture
#bpy.ops.node.add_node(type="ShaderNodeTexNoise", use_transform=True)

# texture coordinate
#bpy.ops.node.add_node(type="ShaderNodeTexCoord", use_transform=True)

# mix RGB
#bpy.ops.node.add_node(type="ShaderNodeMixRGB", use_transform=True)

#mix RGB add
#bpy.data.materials["grass_test_LOD0_u0_v0"].node_tree.nodes["Mix"].blend_type = 'ADD'

#mix RGB subtract
#bpy.data.materials["grass_test_LOD0_u0_v0"].node_tree.nodes["Mix.001"].blend_type = 'SUBTRACT'

#sub fac = 1
#bpy.data.materials["grass_test_LOD0_u0_v0"].node_tree.nodes["Mix.001"].inputs[0].default_value = 1

#add fac = 0.1
#bpy.data.materials["grass_test_LOD0_u0_v0"].node_tree.nodes["Mix"].inputs[0].default_value = 0.1




