import socket
import json


def client_program():
    client_socket = socket.socket()
    client_socket.connect(('127.0.0.1', 12345))

    graph = {
        '1': ['2', '3'],
        '2': ['4', '5'],
        '3': [],
        '4': [],
        '5': [],
        'start': '1'
    }
    data = json.dumps(graph)
    client_socket.send(data.encode())

    client_socket.close()


if __name__ == "__main__":
    client_program()
