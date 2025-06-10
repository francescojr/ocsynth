import bpy

class VIEW3D_PT_syntheyes_importer(bpy.types.Panel):
    bl_label = "OCSynth"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "OCSynth" 

    def draw(self, context):
        layout = self.layout
        layout.operator("import_scene.syntheyes_py", icon='SCRIPT')

# Adiciona funções de registro para o auto_load
classes = [VIEW3D_PT_syntheyes_importer]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
