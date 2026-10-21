# Task 1: Server receives and prints the client's IP and device name
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

# 4. Create Socket object
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
print("Before Bind:", server)

# 5. Attach/Bind socket address to socket
server.bind(server_socket_address)
print("After Bind:", server)

# 6. Activate Server
server.listen()
print("Server is listening for connections...")

# 7. Accept connection from client
def handle_client(conn, addr):
    print("\nConnected to client at", addr)
    connected = True

    while connected:
        message_length = conn.recv(buffer).decode(format)
        if not message_length:
            break

        message_length = int(message_length)
        msg = conn.recv(message_length).decode(format)
        if msg == disconnected or msg.lower() == "end":
            conn.send("Goodbye. It was nice to serve you.".encode(format))
            print("Terminating connection with", addr)
            connected = False
        else:
            # Print client IP and device name as received from client
            print("[CLIENT INFO RECEIVED]")
            print(msg)
            conn.send("Server received client IP and device name successfully.".encode(format))

    conn.close()

while True:
    conn, addr = server.accept()
    handle_client(conn, addr)
