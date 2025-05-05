import os
import shutil
from pathlib import Path
from ..utils.decorators import require_root
from ..utils.style import color_print

def cat_command(shell, *args):
    """Print file content"""
    if not args:
        color_print("Usage: cat <file>", "red")
        return
    try:
        path = shell._resolve_path(args[0])
        with open(path, 'r') as f:
            print(f.read())
    except FileNotFoundError:
        color_print(f"File not found: {args[0]}", "red")
    except Exception as e:
        color_print(f"Error reading file: {e}", "red")

def mkdir_command(shell, *args):
    """Create directory"""
    if not args:
        color_print("Usage: mkdir <directory>", "red")
        return
    
    try:
        path = shell._resolve_path(args[0])
        os.makedirs(path, exist_ok=True)
        color_print(f"Directory created: {path}", "green")
    except Exception as e:
        color_print(f"Error creating directory: {e}", "red")

def rm_command(shell, *args):
    """Remove files/directories"""
    if not args:
        color_print("Usage: rm [-r] <file/directory>", "red")
        return
        
    recursive = '-r' in args
    targets = [a for a in args if a != '-r']
    
    for target in targets:
        try:
            path = shell._resolve_path(target)
            if os.path.isdir(path):
                if recursive:
                    shutil.rmtree(path)
                    color_print(f"Directory removed: {path}", "green")
                else:
                    color_print(f"Error: {target} is a directory (use -r to remove directories)", "yellow")
            else:
                os.remove(path)
                color_print(f"File removed: {path}", "green")
        except FileNotFoundError:
            color_print(f"Error: {target} not found", "red")
        except Exception as e:
            color_print(f"Error removing {target}: {e}", "red")

def cp_command(shell, *args):
    """Copy files/directories"""
    if len(args) < 2:
        color_print("Usage: cp <source> <destination>", "red")
        return
    try:
        src = shell._resolve_path(args[0])
        dst = shell._resolve_path(args[1])
        
        if os.path.isdir(src):
            shutil.copytree(src, dst)
            color_print(f"Directory copied: {src} -> {dst}", "green")
        else:
            shutil.copy2(src, dst)
            color_print(f"File copied: {src} -> {dst}", "green")
    except FileNotFoundError:
        color_print("Error: Source file/directory not found", "red")
    except Exception as e:
        color_print(f"Error copying: {e}", "red")

def mv_command(shell, *args):
    """Move/rename files"""
    if len(args) < 2:
        color_print("Usage: mv <source> <destination>", "red")
        return
    try:
        src = shell._resolve_path(args[0])
        dst = shell._resolve_path(args[1])
        shutil.move(src, dst)
        color_print(f"Moved: {src} -> {dst}", "green")
    except FileNotFoundError:
        color_print("Error: Source file not found", "red")
    except Exception as e:
        color_print(f"Error moving file: {e}", "red")

def ls_command(shell, *args):
    """List directory contents"""
    path = shell.current_dir if shell.current_dir != '~' else os.path.expanduser('~')
    if args:
        path = shell._resolve_path(args[0])
    
    try:
        items = os.listdir(path)
        for item in items:
            full_path = os.path.join(path, item)
            if os.path.isdir(full_path):
                color_print(f"{item}/", "blue")
            elif os.access(full_path, os.X_OK):
                color_print(item, "green")
            else:
                print(item)
    except FileNotFoundError:
        color_print(f"Directory not found: {path}", "red")
    except Exception as e:
        color_print(f"Error listing directory: {e}", "red")