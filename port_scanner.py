# PORT SCANNER 

# The objective of this script is to create a simple port scanner that checks for open ports on a target host.

# Import the socket library that allows us to create network connections from Python
import socket

# Ask the user for the target host to scan
ip = input("Enter the IP address to scan: ")

# Scans a range of ports and verifies their status: open or closed
for port in range(0, 65535):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Specifies the use of IPv4 (AF_INET) and TCP (SOCK_STREAM)
    sock.settimeout(5) 

    result = sock.connect_ex((ip, port))

    if result == 0:
        print("Open port found:", port)
        sock.close()
    else:
        print("Closed port found:", port)
        sock.close()
