import bpy

class SyntheyesImporterProperties(bpy.types.PropertyGroup):
    auto_center: bpy.props.BoolProperty(
        name="Centralizar Cena",
        default=True
    )

# Adiciona funções de registro para o auto_load
classes = [SyntheyesImporterProperties]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
