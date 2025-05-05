import sys
from pathlib import Path

# Добавляем родительскую директорию в путь
sys.path.append(str(Path(__file__).parent.parent))

from angelbox.core.boot import BootLoader

if __name__ == "__main__":
    boot_loader = BootLoader()
    boot_loader.start()