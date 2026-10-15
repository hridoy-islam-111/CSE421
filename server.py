# We will create a socket 
# adddress first

import socket

# 1. Definging the port number
port=5000

# 2. Determine the device name
hostname=socket.gethostname()
host_ip_address=socket.gethostbyname(hostname)

print("The host name is: ",hostname)
print("The host IP address is: ",host_ip_address)