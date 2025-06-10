import importlib
import inspect
import pkgutil
import bpy

class AutoLoad:
    modules = []

    @classmethod
    def init(cls):
        print("[AutoLoad] init")
        cls.modules.clear()

    @classmethod
    def register(cls):
        print(f"[AutoLoad] Registering {len(cls.modules)} modules...")
        for module in cls.modules:
            print(f"[AutoLoad] Registering module: {module.__name__}")
            if hasattr(module, 'register'):
                module.register()

    @classmethod
    def unregister(cls):
        print(f"[AutoLoad] Unregistering {len(cls.modules)} modules...")
        for module in reversed(cls.modules):
            print(f"[AutoLoad] Unregistering module: {module.__name__}")
            if hasattr(module, 'unregister'):
                module.unregister()

def setup_auto_load(namespace):
    import os
    def _get_submodules():
        print(f"[AutoLoad] Searching submodules in: {namespace.__name__}")
        # Se __path__ não existe, tenta usar o diretório do arquivo
        if hasattr(namespace, '__path__'):
            search_path = namespace.__path__
        else:
            search_path = [os.path.dirname(namespace.__file__)]
        found = []
        for _, name, _ in pkgutil.iter_modules(search_path):
            print(f"[AutoLoad] Found submodule: {name}")
            mod = importlib.import_module(f"{namespace.__name__}.{name}")
            found.append(mod)
        return found
    for module in _get_submodules():
        for _, cls in inspect.getmembers(module, inspect.isclass):
            if issubclass(cls, (bpy.types.Operator, bpy.types.Panel, bpy.types.PropertyGroup)):
                print(f"[AutoLoad] Registering module (has Blender class): {module.__name__}")
                AutoLoad.modules.append(module)
                break
