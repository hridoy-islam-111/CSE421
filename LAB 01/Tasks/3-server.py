# Task 3: Multi-threaded server to handle multiple clients simultaneously and count vowels
import socket
import threading

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

# 7. Accept and handle connection from client via multi-threading
def handle_clients(conn, addr):
    print(f"\n[NEW CONNECTION] Connected to {addr}")
    connected = True

    while connected:
        message_length = conn.recv(buffer).decode(format)
        if not message_length:
            break
        print(f"[{addr}] Length of the message is {message_length}")

        message_length = int(message_length)
        msg = conn.recv(message_length).decode(format)
        if msg == disconnected or msg.lower() == "end":
            conn.send("Goodbye. It was nice to serve you.".encode(format))
            print(f"[DISCONNECT] Terminating connection with {addr}")
            connected = False
        else:
            vowels = "aeiouAEIOU"
            total = 0
            for char in msg:
                if char in vowels:
                    total += 1

            if total == 0:
                conn.send("Not enough vowels".encode(format))
            elif total <= 2:
                conn.send("Enough vowels I guess".encode(format))
            else:
                conn.send("Too many vowels".encode(format))

    conn.close()

while True:
    conn, addr = server.accept()
    thread = threading.Thread(target=handle_clients, args=(conn, addr))
    thread.start()
    print(f"[ACTIVE CLIENTS] {threading.active_count() - 1}")
