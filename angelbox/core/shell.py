import os
import importlib
from pathlib import Path
from colorama import Fore, Style
from ..utils.decorators import require_root

class AngelShell:
    def __init__(self, user, config_path):
        self.user = user
        self.config_path = config_path
        self.current_dir = user.get('home', '~')
        self.prompt = self._create_prompt()
        self.commands = self._load_commands()
        
    def _create_prompt(self):
        username = self.user['username']
        pc_name = "AngelBox"
        prompt_char = '%' if self.user.get('is_root', False) else '$'
        color = Fore.RED if self.user.get('is_root', False) else Fore.CYAN
        
        return (
            f"{Fore.BLUE}{username}{Style.RESET_ALL}@"
            f"{Fore.CYAN}{pc_name}{Style.RESET_ALL}:"
            f"{Fore.GREEN}{self.current_dir}{Style.RESET_ALL}"
            f"{color}{prompt_char}{Style.RESET_ALL}>> "
        )
        
    def _resolve_path(self, path):
        """Convert relative paths to absolute"""
        if path.startswith('~'):
            return os.path.expanduser(path)
        elif not os.path.isabs(path):
            base = os.path.expanduser('~') if self.current_dir == '~' else self.current_dir
            return os.path.abspath(os.path.join(base, path))
        return path
        
    def _load_commands(self):
        """Initialize all available commands"""
        from ..commands import base, files, system, network, pkg, admin, process
        
        commands = {
            # Base commands
            'help': base.help_command,
            'exit': base.exit_command,
            'clear': base.clear_command,
            'ls': files.ls_command,
            'cd': base.cd_command,
            
            # File operations
            'cat': files.cat_command,
            'mkdir': files.mkdir_command,
            'rm': files.rm_command,
            'cp': files.cp_command,
            'mv': files.mv_command,
            
            # System info
            'date': system.date_command,
            'uname': system.uname_command,
            'df': system.df_command,
            'free': system.free_command,
            
            # Network
            'ping': network.ping_command,
            'wget': network.wget_command,
            
            # Process management
            'ps': process.ps_command,
            'kill': process.kill_command,
            'bg': process.bg_command,
            
            # Package manager
            'pkg': pkg.pkg_manager,
            
            # Administration
            'su': admin.su_command,
            'useradd': admin.useradd_command
        }
        
        # Добавляем passwd_command только если она существует
        if hasattr(admin, 'passwd_command'):
            commands['passwd'] = admin.passwd_command
            
        return commands
        
    def run(self):
        """Main shell loop"""
        while True:
            try:
                user_input = input(self.prompt).strip()
                if not user_input:
                    continue
                    
                cmd, *args = user_input.split()
                
                if cmd in self.commands:
                    try:
                        self.commands[cmd](self, *args)
                    except Exception as e:
                        print(f"{Fore.RED}Error executing command: {e}{Style.RESET_ALL}")
                else:
                    print(f"{Fore.RED}Command not found: {cmd}{Style.RESET_ALL}")
                    
            except KeyboardInterrupt:
                print(f"\n{Fore.YELLOW}Use 'exit' to quit{Style.RESET_ALL}")
            except EOFError:
                print(f"\n{Fore.YELLOW}Use 'exit' to quit{Style.RESET_ALL}")
            except Exception as e:
                print(f"{Fore.RED}Fatal error: {e}{Style.RESET_ALL}")
                raise