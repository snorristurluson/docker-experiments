import argparse
import socket


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("port", type=int)

    args = parser.parse_args()

    listener = socket.socket()
    listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listener.bind(("0.0.0.0", args.port))
    listener.listen()

    while True:
        print("echo server waiting for connection")
        connection, address = listener.accept()
        while True:
            data = connection.recv(4096).decode()
            if data:
                print(data)
                connection.send(("Echo: " + data).encode())
            else:
                break


if __name__ == "__main__":
    main()
