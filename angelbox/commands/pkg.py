import json
import importlib
import pip
from pathlib import Path

def pkg_manager(shell, *args):
    """Package manager for AngelBox OS"""
    if not args:
        print("Usage: pkg [install|remove|list] [package]")
        return
        
    root_dir = Path(__file__).parent.parent.parent.parent
    config_path = root_dir / "angelbox" / "data" / "config.json"
    
    with open(config_path, 'r') as f:
        config = json.load(f)
        
    if args[0] == "install" and len(args) > 1:
        package = args[1]
        try:
            if hasattr(pip, 'main'):
                pip.main(['install', package])
            else:
                pip._internal.main(['install', package])
                
            config['packages'].append(package)
            with open(config_path, 'w') as f:
                json.dump(config, f)
            print(f"Package {package} installed successfully!")
        except Exception as e:
            print(f"Error installing package: {e}")
            
    elif args[0] == "remove" and len(args) > 1:
        package = args[1]
        try:
            if hasattr(pip, 'main'):
                pip.main(['uninstall', '-y', package])
            else:
                pip._internal.main(['uninstall', '-y', package])
                
            config['packages'] = [p for p in config['packages'] if p != package]
            with open(config_path, 'w') as f:
                json.dump(config, f)
            print(f"Package {package} removed successfully!")
        except Exception as e:
            print(f"Error removing package: {e}")
            
    elif args[0] == "list":
        print("Installed packages:")
        for pkg in config['packages']:
            print(f"  {pkg}")
    else:
        print("Invalid command. Usage: pkg [install|remove|list] [package]")