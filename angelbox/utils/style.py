from colorama import Fore, Style

def color_print(text, color):
    """Print colored text"""
    colors = {
        'red': Fore.RED,
        'green': Fore.GREEN,
        'yellow': Fore.YELLOW,
        'blue': Fore.BLUE,
        'cyan': Fore.CYAN,
        'magenta': Fore.MAGENTA
    }
    print(f"{colors.get(color, '')}{text}{Style.RESET_ALL}")