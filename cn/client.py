import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get local machine name
host = socket.gethostname()

# Reserve a port for your service
port = 12345

# Connect to the server
client_socket.connect((host, port))

# Send data
message = "Hello, Server!"
client_socket.sendall(message.encode())

# Receive the response
data = client_socket.recv(1024)
print(f"Received: {data.decode()}")

# Clean up the connection
client_socket.close()

