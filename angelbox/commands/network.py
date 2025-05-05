import socket
import requests
from urllib.parse import urlparse
from ..utils.style import color_print

def ping_command(shell, *args):
    """Ping a host"""
    if not args:
        print("Usage: ping <host>")
        return
    
    host = args[0]
    try:
        ip = socket.gethostbyname(host)
        color_print(f"PING {host} ({ip})", "cyan")
        # В реальной системе здесь была бы отправка ICMP пакетов
        color_print(f"{host} is reachable", "green")
    except Exception as e:
        color_print(f"Error pinging {host}: {e}", "red")

def wget_command(shell, *args):
    """Download file from URL"""
    if not args:
        print("Usage: wget <url> [output_file]")
        return
    
    url = args[0]
    output = args[1] if len(args) > 1 else urlparse(url).path.split('/')[-1]
    
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        
        with open(output, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        color_print(f"Downloaded {url} to {output}", "green")
    except Exception as e:
        color_print(f"Error downloading {url}: {e}", "red")