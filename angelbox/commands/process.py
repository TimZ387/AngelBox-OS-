import os
import signal
import subprocess
import psutil
from ..utils.decorators import require_root
from ..utils.style import color_print

def ps_command(shell, *args):
    """List running processes"""
    try:
        for proc in psutil.process_iter(['pid', 'name', 'username']):
            color_print(f"{proc.info['pid']:>6} {proc.info['username']:<15} {proc.info['name']}", "yellow")
    except Exception as e:
        print(f"Error: {e}")

def kill_command(shell, *args):
    """Kill process by PID"""
    if not args:
        print("Usage: kill <pid>")
        return
    
    try:
        pid = int(args[0])
        os.kill(pid, signal.SIGTERM)
        color_print(f"Process {pid} terminated", "green")
    except Exception as e:
        color_print(f"Error killing process: {e}", "red")

def bg_command(shell, *args):
    """Run command in background"""
    if not args:
        print("Usage: bg <command> [args...]")
        return
    
    try:
        proc = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        color_print(f"Started process {proc.pid} in background", "cyan")
        return proc
    except Exception as e:
        color_print(f"Error: {e}", "red")