# Task 4: Server calculates salary based on hours worked
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

# 7. Accept connection from client and handle salary calculation
def handle_client(conn, addr):
    print("\nConnected to client at", addr)
    connected = True

    while connected:
        message_length = conn.recv(buffer).decode(format)
        if not message_length:
            break
        print("Length of the message is", message_length)

        message_length = int(message_length)
        msg = conn.recv(message_length).decode(format)
        if msg == disconnected or msg.lower() == "end":
            conn.send("Goodbye. It was nice to serve you.".encode(format))
            print("Terminating connection with", addr)
            connected = False
        else:
            try:
                hours = float(msg)
                # Salary calculation:
                # - <= 40 hours: Tk 200 per hour
                # - > 40 hours: Tk 8000 + Tk 300 for each hour over 40
                if hours <= 40:
                    salary = hours * 200
                else:
                    salary = 8000 + (hours - 40) * 300

                # Format as integer if whole number
                if salary.is_integer():
                    salary = int(salary)

                reply = f"Total salary is: Tk {salary}"
                conn.send(reply.encode(format))
            except ValueError:
                conn.send("Invalid input! Please enter a numeric value for hours worked.".encode(format))

    conn.close()

while True:
    conn, addr = server.accept()
    handle_client(conn, addr)
