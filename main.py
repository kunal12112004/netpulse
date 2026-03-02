import socket
import os

def get_network_info():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    print(f"--- Network Info ---")
    print(f"Hostname: {hostname}")
    print(f"Local IP: {ip_address}")

def ping_server(address):
    print(f"\n--- Pinging {address} ---")
    # This works on Windows and Linux
    response = os.system(f"ping -n 1 {address}" if os.name == 'nt' else f"ping -c 1 {address}")
    if response == 0:
        print(f"Result: {address} is UP!")
    else:
        print(f"Result: {address} is DOWN!")

if __name__ == "__main__":
    get_network_info()
    target = input("\nEnter a website to ping (e.g., google.com): ")
    ping_server(target)
