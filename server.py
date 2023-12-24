import socket
import json
import multiprocessing as mp
from collections import deque
import threading
import select

exit_command = False
active_threads = []


def bfs(graph, start, queue, visited):
    """Process BFS for the node and offload adjacent nodes to the queue for parallel processing"""
    try:
        adj_nodes = deque(graph[start])
    except KeyError:
        return  # Exit function if the start node is not in the graph

    visited.append(start)

    while adj_nodes:
        node = adj_nodes.popleft()
        if node not in visited:
            visited.append(node)
            queue.put(node)


def parallel_bfs(graph, start):
    """Use multiprocessing to process BFS on multiple nodes in parallel"""
    with mp.Manager() as manager:
        visited = manager.list([start])
        queue = mp.Queue()
        processes = []

        bfs(graph, start, queue, visited)
        while not queue.empty():
            p = mp.Process(target=bfs, args=(graph, queue.get(), queue, visited))
            p.start()
            processes.append(p)

        for p in processes:
            p.join()

        return list(visited)


def handle_client(connection):
    data = connection.recv(1024).decode()
    graph = json.loads(data)
    print("Graph received from client: ", graph)
    start = graph['start']
    del graph['start']
    visited = parallel_bfs(graph, start)

    connection.send(json.dumps(visited).encode())
    connection.close()


def exit_check():
    global exit_command
    while True:
        if input('') == 'exit':
            exit_command = True
            break


def server_program():
    threading.Thread(target=exit_check).start()

    port = 12345
    server_socket = socket.socket()
    server_socket.bind(('127.0.0.1', port))
    server_socket.listen(1)

    print("Server is ready and listening. Type 'exit' at any time to shut down the server.")
    inputs = [server_socket]

    global exit_command
    while True:
        readable, _, _ = select.select(inputs, [], [], 0.1)
        if exit_command:
            print("Exit command received. Waiting for all active connections to finish...")
            for thread in active_threads:
                thread.join()
            print("All active connections finished. Shutting down server.")
            server_socket.close()
            break

        if readable:
            connection, address = server_socket.accept()
            client_thread = threading.Thread(target=handle_client, args=(connection,))
            active_threads.append(client_thread)
            client_thread.start()


if __name__ == "__main__":
    server_program()
