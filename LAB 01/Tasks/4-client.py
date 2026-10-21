# Task 4: Client provides hours worked to calculate salary
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
    print("Server Response:", client.recv(2048).decode(format))

while True:
    hours_input = input("\nEnter the number of hours worked (or 'end' to exit): ")
    if hours_input.lower() == "end":
        msg_to_be_sent(disconnected)
        print("Terminating connection with the server")
        break
    else:
        msg_to_be_sent(hours_input)
