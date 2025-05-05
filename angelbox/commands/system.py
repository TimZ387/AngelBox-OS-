import os
import platform
import time
from ..utils.style import color_print

def date_command(shell, *args):
    """Show current date and time"""
    color_print(time.strftime("%a %b %d %H:%M:%S %Z %Y"), "green")

def uname_command(shell, *args):
    """Show system information"""
    info = {
        "System": platform.system(),
        "Node": platform.node(),
        "Release": platform.release(),
        "Version": platform.version(),
        "Machine": platform.machine(),
        "Processor": platform.processor()
    }
    
    for k, v in info.items():
        color_print(f"{k:<10}: {v}", "cyan")

def df_command(shell, *args):
    """Show disk usage"""
    try:
        import psutil
        partitions = psutil.disk_partitions()
        for part in partitions:
            usage = psutil.disk_usage(part.mountpoint)
            color_print(f"{part.device:<20} {part.mountpoint:<15} "
                       f"{usage.percent:>5}% {usage.free//(1024*1024):<5}MB free", "yellow")
    except ImportError:
        print("Install psutil package for this feature")

def free_command(shell, *args):
    """Show memory usage"""
    try:
        import psutil
        mem = psutil.virtual_memory()
        color_print(f"Total: {mem.total//(1024*1024)}MB", "blue")
        color_print(f"Used:  {mem.used//(1024*1024)}MB ({mem.percent}%)", "red")
        color_print(f"Free:  {mem.free//(1024*1024)}MB", "green")
    except ImportError:
        print("Install psutil package for this feature")