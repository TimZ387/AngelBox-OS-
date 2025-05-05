import json
import getpass
from pathlib import Path
from colorama import Fore, Style
from ..utils.decorators import require_root

def su_command(shell, *args):
    """Switch to root user"""
    if shell.user.get('is_root', False):
        print(f"{Fore.YELLOW}You are already root!{Style.RESET_ALL}")
        return
        
    password = getpass.getpass("Password: ")
    
    try:
        with open(shell.config_path, 'r') as f:
            config = json.load(f)
    except Exception as e:
        print(f"{Fore.RED}Error loading config: {e}{Style.RESET_ALL}")
        return
        
    for user in config.get('users', []):
        if user.get('is_root', False) and user['password'] == password:
            shell.user = user
            shell.prompt = shell._create_prompt()
            print(f"{Fore.GREEN}Now you are root!{Style.RESET_ALL}")
            return
            
    print(f"{Fore.RED}Invalid password!{Style.RESET_ALL}")

@require_root
def useradd_command(shell, *args):
    """Add new user"""
    if len(args) < 1:
        print(f"{Fore.RED}Usage: useradd <username>{Style.RESET_ALL}")
        return
        
    username = args[0]
    password = getpass.getpass(f"Password for {username}: ")
    
    try:
        with open(shell.config_path, 'r') as f:
            config = json.load(f)
    except Exception as e:
        print(f"{Fore.RED}Error loading config: {e}{Style.RESET_ALL}")
        return
        
    if any(u['username'] == username for u in config.get('users', [])):
        print(f"{Fore.YELLOW}User {username} already exists!{Style.RESET_ALL}")
        return
        
    config['users'].append({
        'username': username,
        'password': password,
        'home': str(Path.home()),
        'is_root': False,
        'user_id': len(config['users']) + 1000
    })
    
    try:
        with open(shell.config_path, 'w') as f:
            json.dump(config, f, indent=4)
        print(f"{Fore.GREEN}User {username} created successfully!{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}Error saving config: {e}{Style.RESET_ALL}")

@require_root
def passwd_command(shell, *args):
    """Change user password"""
    if len(args) > 1:
        print(f"{Fore.RED}Usage: passwd [username]{Style.RESET_ALL}")
        return
        
    try:
        with open(shell.config_path, 'r+') as f:
            config = json.load(f)
            
            # Determine which user to change
            username = args[0] if args else shell.user['username']
            
            # Find the user
            user = next((u for u in config['users'] if u['username'] == username), None)
            if not user:
                print(f"{Fore.RED}User {username} not found!{Style.RESET_ALL}")
                return
                
            # Verify current password if changing other user's password
            if not shell.user.get('is_root', False) and username != shell.user['username']:
                print(f"{Fore.RED}You can only change your own password!{Style.RESET_ALL}")
                return
                
            # Get new password
            new_password = getpass.getpass("New password: ")
            confirm_password = getpass.getpass("Retype new password: ")
            
            if new_password != confirm_password:
                print(f"{Fore.RED}Passwords don't match!{Style.RESET_ALL}")
                return
                
            # Update password
            user['password'] = new_password
            f.seek(0)
            json.dump(config, f, indent=4)
            f.truncate()
            
            print(f"{Fore.GREEN}Password updated successfully!{Style.RESET_ALL}")
            
    except Exception as e:
        print(f"{Fore.RED}Error changing password: {e}{Style.RESET_ALL}")