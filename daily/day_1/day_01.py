import socket
import platform
import subprocess

def get_my_ip():
    """Get the local IP address of this machine"""
    s = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8" , 80))
        ip = s.getsockname()[0]
    except Exception:
        ip ="unable to determine"
    finally:
        s.close()
    return ip

def get_hostname():
    """Get the name of this computer on the network"""
    return socket.gethostname()

def ping_host(host):
    """Ping a host and return True if reachable"""
    #Different ping command for windows vs linux/mac
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param , "4" , host]
    result = subprocess.run(command , capture_output=True, text=True)
    return result.returncode == 0

print("__" * 40)
print(" DAY 1 - NETWORK DISCOVERY TOOL")
print("__"*20)

my_ip = get_my_ip()
my_hostname = get_hostname()

print(f"MY Hostname : {my_hostname}")
print(f"MY IP : {my_hostname}")

#Derive the network base (e.g., 192.168.1)
ip_parts = my_ip.split(".")
network = f"{ip_parts[0]}.{ip_parts[1]}.{ip_parts[2]}"

print(f"Network : {network}.0/24")
print(f"\n Testing connectivity to key servers...")
print("__" * 40)

targets = {
    "Google DNS" : "8.8.8.8",
    "Cloudflare DNS" : "1.1.1.1",
    "Your Router" : f"{network}.1", #Routers are usually .1
}

for name , host in targets.items():
    status = "REACHABLE" if ping_host(host) else "UNREACHABLE"
    print(f" {name:<20}({host:<15}) -> {status}")

print("__" * 20)
print("SCAN COMPLETE.")
print("__" * 20)