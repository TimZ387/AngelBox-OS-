import os

def help_command(shell, *args):
    """Show available commands"""
    print("Available commands:")
    for cmd in shell.commands:
        print(f"  {cmd}")

def exit_command(shell, *args):
    """Exit the shell"""
    print("Goodbye!")
    exit(0)

def clear_command(shell, *args):
    """Clear the screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def ls_command(shell, *args):
    """List directory contents"""
    path = shell.current_dir if shell.current_dir != '~' else os.path.expanduser('~')
    try:
        print("\n".join(os.listdir(path)))
    except Exception as e:
        print(f"Error: {e}")

def cd_command(shell, *args):
    """Change directory"""
    if not args:
        shell.current_dir = '~'
    else:
        new_dir = args[0]
        if new_dir == '~':
            shell.current_dir = '~'
        else:
            try:
                abs_path = os.path.abspath(os.path.join(
                    os.path.expanduser('~') if shell.current_dir == '~' else shell.current_dir,
                    new_dir
                ))
                if os.path.isdir(abs_path):
                    shell.current_dir = abs_path
                else:
                    print(f"Directory not found: {new_dir}")
            except Exception as e:
                print(f"Error: {e}")
    shell.prompt = shell._create_prompt()