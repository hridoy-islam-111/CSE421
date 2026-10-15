# We will create a socket 
# adddress first

import socket

# 1. Definging the port number
port=5000
format = "utf-8"
buffer = 16
disconnected = "End"


# 2. Determine the device name
hostname=socket.gethostname()
host_ip_address=socket.gethostbyname(hostname)

print("The host name is: ",hostname)
print("The host IP address is: ",host_ip_address)


# 3. Make a socket address
server_socket_address=(host_ip_address,port)

# 4. Create Socket object
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

print("Before Bind:", server)

# 5. Attach/Bind socket address to socket
server.bind(server_socket_address)
print("After Bind:", server)

# 6. Active Server
server.listen()
print("Server is listening for connections...")

# 7. Accept connection from client
while True:
    conn, addr = server.accept()
    print("Connected to", addr)
    connected = True
    # (Done already)

    while connected:
        message_length = conn.recv(buffer).decode(format)
        print("Length of the message is", message_length)


        if message_length:
            message_length = int(message_length)
            msg = conn.recv(message_length).decode(format)
            if msg == disconnected:
                conn.send("Goodbye. It was nice to serve you.".encode(format))
                print("Terminating connection with", addr)
                connected = False
            else:
                print(msg)
                conn.send("I have received your message".encode(format))
    conn.close()
