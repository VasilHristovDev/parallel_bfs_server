import socket
import json


def client_program():
    client_socket = socket.socket()
    client_socket.connect(('127.0.0.1', 12345))

    # Accept user input for the graph
    graph = eval(input("Enter the graph: "))

    data = json.dumps(graph)
    client_socket.send(data.encode())

    response = client_socket.recv(1024).decode()
    visited = json.loads(response)
    print("Nodes visited in BFS order: ", visited)

    client_socket.close()


if __name__ == "__main__":
    client_program()
