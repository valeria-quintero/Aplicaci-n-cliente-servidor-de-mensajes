import socket
import threading

HOST = "0.0.0.0"
PORT = 8000

clients = []  # Lista de clientes conectados

def broadcast(message, sender_socket=None):
    """Envia el mensaje a todos los clientes excepto al que lo mandó"""
    for client in clients:
        if client != sender_socket:
            try:
                client.sendall(message.encode("utf-8"))
            except:
                clients.remove(client)

def handle_client(conn, addr):
    print(f"[+] Cliente conectado: {addr}")
    while True:
        try:
            data = conn.recv(1024).decode("utf-8")
            if not data:
                break

            parts = data.split("|", 1)
            command = parts[0]
            content = parts[1] if len(parts) > 1 else ""

            if command == "MSG":
                print(f"[{addr}] dice: {content}")
                broadcast(f"{addr} dice: {content}", conn)

            elif command == "EXIT":
                print(f"[-] Cliente {addr} se desconectó")
                broadcast(f"SERVIDOR: Cliente {addr} salió del chat")
                break

        except:
            break

    conn.close()
    if conn in clients:
        clients.remove(conn)

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    print(f"Servidor escuchando en {HOST}:{PORT}")

    while True:
        conn, addr = server_socket.accept()
        clients.append(conn)
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

if __name__ == "__main__":
    start_server()
