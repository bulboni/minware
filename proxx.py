import socket
import threading

def handle_client(client_socket, remote_host, remote_port):
    remote_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    remote_socket.connect((remote_host, remote_port))
    
    def forward(src, dst):
        while True:
            try:
                data = src.recv(8192)
                if not data:
                    print("[*] Connection closed by client")
                    break
                dst.send(data)
            except BrokenPipeError:
                print("[*] Broken pipe error occurred")
                break
    
    client_thread = threading.Thread(target=forward, args=(client_socket, remote_socket))
    remote_thread = threading.Thread(target=forward, args=(remote_socket, client_socket))
    
    client_thread.start()
    remote_thread.start()
    
    client_thread.join()
    remote_thread.join()
    
    client_socket.close()
    remote_socket.close()

def main():
    local_host = "0.0.0.0"
    local_port = 4090
    remote_host = "cpu-pool.com"
    remote_port = 63388
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((local_host, local_port))
    server.listen(100)
    
    print(f"[*] Listening on {local_host}:{local_port}")
    
    while True:
        client_socket, addr = server.accept()
        print(f"[*] Accepted connection from {addr[0]}:{addr[1]}")
        
        # Forwarding data from client to remote server
        client_to_remote_thread = threading.Thread(target=handle_client, args=(client_socket, remote_host, remote_port))
        client_to_remote_thread.start()
        
        # Forwarding data from remote server to client
        remote_to_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        remote_to_client_socket.connect((remote_host, remote_port))
        remote_to_client_thread = threading.Thread(target=handle_client, args=(remote_to_client_socket, addr[0], addr[1]))
        remote_to_client_thread.start()

if __name__ == "__main__":
    main()
