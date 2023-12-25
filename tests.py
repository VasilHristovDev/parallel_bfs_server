import unittest
from multiprocessing import Manager, Queue
import server

bfs = server.bfs


class TestBFS(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()
        self.manager = Manager()
        self.visited = self.manager.list()

    def test_bfs(self):
        graph = {
            '1': ['2', '3'],
            '2': ['4', '5'],
            '3': [],
            '4': [],
            '5': [],
            'start': '1'
        }
        bfs(graph, '1', self.queue, self.visited)
        self.assertListEqual(list(self.visited), ['1', '2', '3'])  # Convert to a Python list

    def test_bfs_empty_graph(self):
        graph = {}
        bfs(graph, '1', self.queue, self.visited)
        self.assertListEqual(list(self.visited), [])

    def test_bfs_no_edges(self):
        graph = {
            '1': [],
            '2': [],
            '3': [],
            '4': [],
            '5': [],
            'start': '1'
        }
        bfs(graph, '1', self.queue, self.visited)
        self.assertListEqual(list(self.visited), ['1'])


if __name__ == '__main__':
    unittest.main()
