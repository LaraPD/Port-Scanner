# PORT SCANNER
# The objective of this script is to create a simple port scanner that checks for open ports on a target host.

# Import the socket library that allows us to create network connections from Python
import socket

# Ask the user for the target host and the range of ports to scan
ip = input("Enter the IP address to scan: ")
start_port = int(input("Enter the starting port: "))
end_port = int(input("Enter the ending port: "))

open_ports = []

print(f"\n🔎 Scanning host {ip}\n" + "..." + "\n")
print("OPEN ports ✅ | CLOSED ports ❌\n")
print("-" * 32)

# Scans a range of ports and verifies their status: open or closed
for port in range(start_port, end_port + 1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Specifies the use of IPv4 (AF_INET) and TCP (SOCK_STREAM)
    sock.settimeout(0.5)
    
    result = sock.connect_ex((ip, port))
    
    if result == 0:
        print(f"Port {port:<5} ✅")
        open_ports.append(port)
    else:
        print(f"Port {port:<5} ❌")
    
    sock.close()

print("-" * 32)

if open_ports:
    print(f"\n🔵 SUMMARY: Open ports {open_ports}")
else:
    print(f"\n🔴 SUMMARY: No open ports found.\n")
print("\n")
