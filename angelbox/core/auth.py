import json
import getpass
from pathlib import Path
from colorama import Fore, Style

class Authentication:
    def __init__(self, data_dir, config_path):
        self.data_dir = data_dir
        self.config_path = config_path
        
    def authenticate(self):
        config = self._load_or_create_config()
            
        if config.get('first_run', True):
            return self._create_admin_user(config)
            
        return self._login_user(config)
    
    def _load_or_create_config(self):
        """Загружает или создает конфигурационный файл"""
        default_config = {
            "first_run": True,
            "users": [],
            "packages": []
        }
        
        try:
            if not self.config_path.exists():
                with open(self.config_path, 'w') as f:
                    json.dump(default_config, f, indent=4)
                return default_config
            
            with open(self.config_path, 'r') as f:
                return json.load(f)
                
        except Exception as e:
            print(f"{Fore.RED}Error loading config: {e}{Style.RESET_ALL}")
            return default_config
    
    def _login_user(self, config):
        """Процесс входа пользователя"""
        self._print_login_header()
        
        username = input(f"{Fore.CYAN}Username:{Style.RESET_ALL} ")
        password = getpass.getpass(f"{Fore.CYAN}Password:{Style.RESET_ALL} ")
        
        for user in config.get('users', []):
            if user['username'] == username and user['password'] == password:
                print(f"{Fore.GREEN}Login successful!{Style.RESET_ALL}")
                return user
                
        print(f"{Fore.YELLOW}Invalid credentials! Starting as guest.{Style.RESET_ALL}")
        return self._create_guest_user()
    
    def _create_admin_user(self, config):
        """Создает администратора при первом запуске"""
        print(f"\n{Fore.CYAN}{Style.BRIGHT}First run! Create admin user:{Style.RESET_ALL}")
        
        while True:
            username = input(f"{Fore.CYAN}Username:{Style.RESET_ALL} ")
            if username:
                break
            print(f"{Fore.YELLOW}Username cannot be empty!{Style.RESET_ALL}")
                
        while True:
            password = getpass.getpass(f"{Fore.CYAN}Password:{Style.RESET_ALL} ")
            if password:
                break
            print(f"{Fore.YELLOW}Password cannot be empty!{Style.RESET_ALL}")
        
        admin_user = {
            'username': username,
            'password': password,
            'home': str(Path.home()),
            'is_root': True,
            'user_id': 0
        }
        
        config['users'].append(admin_user)
        config['first_run'] = False
        
        self._save_config(config)
        
        print(f"\n{Fore.GREEN}Admin user created successfully!{Style.RESET_ALL}")
        return admin_user
    
    def _create_guest_user(self):
        """Создает временного гостевого пользователя"""
        return {
            'username': 'guest',
            'home': str(Path.home()),
            'is_root': False,
            'user_id': 1000
        }
    
    def _save_config(self, config):
        """Сохраняет конфигурацию с обработкой ошибок"""
        try:
            with open(self.config_path, 'w') as f:
                json.dump(config, f, indent=4, ensure_ascii=False)
        except Exception as e:
            print(f"{Fore.RED}Error saving config: {e}{Style.RESET_ALL}")
            raise
    
    def _print_login_header(self):
        print(f"\n{Fore.CYAN}{Style.BRIGHT}")
        print("╔════════════════════════════════════════╗")
        print("║        AngelBox OS Login               ║")
        print("╚════════════════════════════════════════╝")
        print(f"{Style.RESET_ALL}")