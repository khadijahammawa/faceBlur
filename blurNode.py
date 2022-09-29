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




