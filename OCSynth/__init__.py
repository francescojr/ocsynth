bl_info = {
    "name": "OCSynth",
    "author": "jrFrancesco & PerplexityBro",
    "version": (1, 0),
    "blender": (3, 6, 0),
    "location": "View3D > UI > Importar",
    "description": "Importação one-click de scripts Syntheyes",
    "warning": "",
    "category": "Import-Export", 
} 

import sys
from . import auto_load

def register():
    auto_load.AutoLoad.init()
    auto_load.setup_auto_load(sys.modules[__name__])
    auto_load.AutoLoad.register()

def unregister():
    auto_load.AutoLoad.unregister()
