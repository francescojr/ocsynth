import bpy
import os
from .utils import is_valid_syntheyes_script

class IMPORT_OT_syntheyes(bpy.types.Operator):
    bl_idname = "import_scene.syntheyes_py"
    bl_label = "Import Script"
    bl_options = {'REGISTER', 'UNDO'}

    filepath: bpy.props.StringProperty(subtype="FILE_PATH")
    
    filter_glob: bpy.props.StringProperty(  
        default="*.py",
        options={'HIDDEN'}
    )  

    def execute(self, context):
        if not is_valid_syntheyes_script(self.filepath):
            self.report({'ERROR'}, "Arquivo não é um script Syntheyes válido!")
            return {'CANCELLED'}

        try:
            with open(self.filepath, 'r') as file:
                exec(file.read(), {'bpy': bpy, '__name__': '__main__'})
            self.report({'INFO'}, "Importação concluída!")
        except Exception as e:
            self.report({'ERROR'}, f"Erro na execução: {str(e)}")
            return {'CANCELLED'}

        return {'FINISHED'}

    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}

# Adiciona funções de registro para o auto_load
classes = [IMPORT_OT_syntheyes]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
