# Task 1: Client informs the server of client's IP and device name upon connection
import socket

# 1. Defining the port number
port = 5050
format = "utf-8"
buffer = 16
disconnected = "End"

# 2. Determine the device name
hostname = socket.gethostname()
host_ip_address = socket.gethostbyname(hostname)

print("The host name is: ", hostname)
print("The host IP address is: ", host_ip_address)

# 3. Make a socket address
server_socket_address = (host_ip_address, port)

# 4. Create Client Socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Before Connect:", client)

# 5. Connect to the server
client.connect(server_socket_address)
print("After Connect:", client)

# Helper Codes
def msg_to_be_sent(msg):
    message = msg.encode(format)
    msg_length = len(message)
    msg_length = str(msg_length).encode(format)
    msg_length += b" " * (buffer - len(msg_length))

    client.send(msg_length)
    client.send(message)
    print(client.recv(2048).decode(format))

# Send client IP and device name to the server
info_msg = f"Client's IP Address: {host_ip_address} and Device Name: {hostname}"
print("\nInforming the server of client's IP and device name...")
msg_to_be_sent(info_msg)

# Terminate connection
print("Terminating connection with the server...")
msg_to_be_sent(disconnected)
