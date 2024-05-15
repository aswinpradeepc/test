import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get local machine name
host = socket.gethostname()

# Reserve a port for your service
port = 12345

# Bind the socket to the host and port
server_socket.bind((host, port))

# Listen for incoming connections
server_socket.listen(5)

print(f"Server listening on {host}:{port}")

num = 0

while True:
    # Wait for a connection
    client_socket, addr = server_socket.accept()
    print(f"Got connection from {addr}")

    # Receive the data in small chunks and print it
    data = client_socket.recv(1024)
    print(f"Received: {data.decode()}")

    # Send a response
    response = "response :" + str(num)
    num = num + 1
    client_socket.sendall(response.encode())

    # Clean up the connection
    client_socket.close()
