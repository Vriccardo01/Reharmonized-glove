import socket

def start_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Server listening on {host}:{port}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")
        data = client_socket.recv(1024)
        if data:
            print(f"Received data: {data.decode('utf-8')}")
        client_socket.close()

if __name__ == "__main__":
    host = '0.0.0.0'  # ascolta su tutte le interfacce di rete disponibili
    port = 12345
    start_server(host, port)