import socket
import json


def client_program():
    port = 12345
    client_socket = socket.socket()
    client_socket.connect(('127.0.0.1', port))

    # Accept user input for the graph in json format
    # Example input:
    # {'1': ['2', '3'], '2': ['4', '5'], '3': [], '4': [], '5': [], 'start': '1'}
    graph = eval(input("Enter the graph: "))

    data = json.dumps(graph)
    client_socket.send(data.encode())

    response = client_socket.recv(1024).decode()
    visited = json.loads(response)
    print("Nodes visited in BFS order: ", visited)

    client_socket.close()


if __name__ == "__main__":
    client_program()
