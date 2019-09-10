import argparse
import socket


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("myport", type=int)
    parser.add_argument("host")
    parser.add_argument("port", type=int)

    args = parser.parse_args()

    print("forwarding server listening on {}".format(args.myport))
    listener = socket.socket()
    listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listener.bind(("0.0.0.0", args.myport))
    listener.listen()

    print("forwarding server connecting to echo server {}:{}".format(args.host, args.port))
    echo = socket.socket()
    echo.connect((args.host, args.port))

    while True:
        print("forwarding server waiting for connection")
        connection, address = listener.accept()
        while True:
            data = connection.recv(4096).decode()
            if data:
                print(data)
                echo.send(("Forwarded: " + data).encode())
                echoed = echo.recv(4096).decode()
                print(echoed)
                connection.send(("Returned: " + echoed).encode())

            else:
                break


if __name__ == "__main__":
    main()
