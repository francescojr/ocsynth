def is_valid_syntheyes_script(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            
            markers = [
                "Syntheyes Python Script",
                "sizzle.exportTrackerCameras",
                "sizzle.exportScene",
                "Blender Exporter:",
                "def syntheyes2blender",
                "obj.location"
            ]
            
            return any(marker in content for marker in markers)
    except (OSError, IOError) as e:
        print(f"[is_valid_syntheyes_script] Erro ao ler arquivo: {e}")
        return False
