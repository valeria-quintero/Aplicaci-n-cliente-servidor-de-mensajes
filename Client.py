import socket
import threading

HOST = "127.0.0.1"  # Cambia si el servidor está en otra PC
PORT = 8000

def receive_messages(client_socket):
    """Hilo para recibir mensajes del servidor"""
    while True:
        try:
            data = client_socket.recv(1024).decode("utf-8")
            if not data:
                break
            print("\n" + data)
        except:
            break

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    # Iniciar hilo para recibir mensajes
    thread = threading.Thread(target=receive_messages, args=(client_socket,))
    thread.start()

    while True:
        message = input()
        if message.lower() == "salir":
            client_socket.sendall("EXIT|".encode("utf-8"))
            break
        else:
            client_socket.sendall(f"MSG|{message}".encode("utf-8"))

    client_socket.close()

if __name__ == "__main__":
    main()
