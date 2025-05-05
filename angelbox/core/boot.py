import json
import os
from pathlib import Path
from colorama import Fore, Style
from .auth import Authentication
from .shell import AngelShell

class BootLoader:
    def __init__(self):
        self.system_name = "AngelBox"
        self.version = "0.3.1"
        self.root_dir = Path(__file__).parent.parent.parent
        self.data_dir = self._init_data_directory()
        self.config_path = self.data_dir / "config.json"
        
    def _init_data_directory(self):
        """Initialize data directory with error handling"""
        data_dir = self.root_dir / "data"
        try:
            data_dir.mkdir(exist_ok=True)
            return data_dir
        except Exception as e:
            print(f"{Fore.RED}FATAL: Cannot create data directory: {e}{Style.RESET_ALL}")
            raise SystemExit(1)

    def start(self):
        self._show_welcome()
        auth = Authentication(self.data_dir, self.config_path)
        user = auth.authenticate()
        shell = AngelShell(user, self.config_path)
        shell.run()

    def _show_welcome(self):
        blue = Fore.CYAN
        bright = Style.BRIGHT
        reset = Style.RESET_ALL
        
        print(f"""
        {blue}{bright}
        ╔══════════════════════════════════════════════════╗
        ║                                                  ║
        ║               AngelBox OS                        ║
        ║               Version {self.version}                    ║
        ║                                                  ║
        ╚══════════════════════════════════════════════════╝
        {reset}
        """)