import socket
import json
import multiprocessing as mp
from collections import deque


def bfs(graph, start, queue, visited):
    """Process BFS for the node and offload adjacent nodes to the queue for parallel processing"""
    adj_nodes = deque(graph[start])
    while adj_nodes:
        node = adj_nodes.popleft()
        if node not in visited:
            visited.append(node)
            print(f"Visited: {node}")
            queue.put(node)


def parallel_bfs(graph, start):
    """Use multiprocessing to process BFS on multiple nodes in parallel"""
    with mp.Manager() as manager:
        visited = manager.list()
        queue = mp.Queue()
        processes = []

        # start BFS from the root node
        bfs(graph, start, queue, visited)
        while not queue.empty():
            p = mp.Process(target=bfs, args=(graph, queue.get(), queue, visited))
            p.start()
            processes.append(p)

        # Ensure all processes have finished execution
        for p in processes:
            p.join()


def server_program():
    server_socket = socket.socket()
    server_socket.bind(('127.0.0.1', 12345))
    server_socket.listen(1)
    print('Server is ready and listening')

    connection, address = server_socket.accept()

    data = connection.recv(1024).decode()
    graph = json.loads(data)
    print("Graph received from client: ", graph)
    start = graph['start']
    del graph['start']
    parallel_bfs(graph, start)

    connection.close()


if __name__ == "__main__":
    server_program()
