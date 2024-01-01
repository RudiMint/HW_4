import socket


def main():
    host = socket.gethostname()
    port = 4000

    client_socket = socket.socket()
    client_socket.connect((host, port))
    message = input("-> ")

    while message.lower().strip() != "bye":
        client_socket.send(message.encode())
        msg = client_socket.recv(1024).decode()
        print(f"from connected user: {msg}")
        message = input("-> ")

    client_socket.close()


if __name__ == "__main__":
    main()
