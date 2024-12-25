import unittest
from bipartite_graph import BipartiteGraph

class TestBipartiteGraph(unittest.TestCase):
    def test_empty_graph(self):
        graph = BipartiteGraph()
        self.assertTrue(graph.is_bipartite())

    def test_single_edge(self):
        graph = BipartiteGraph()
        graph.add_edge(1, 2)
        self.assertTrue(graph.is_bipartite())

    def test_triangle_not_bipartite(self):
        graph = BipartiteGraph()
        graph.add_edge(1, 2)
        graph.add_edge(2, 3)
        graph.add_edge(3, 1)
        self.assertFalse(graph.is_bipartite())

    def test_square_is_bipartite(self):
        graph = BipartiteGraph()
        graph.add_edge(1, 2)
        graph.add_edge(2, 3)
        graph.add_edge(3, 4)
        graph.add_edge(4, 1)
        self.assertTrue(graph.is_bipartite())

    def test_partite_sets(self):
        graph = BipartiteGraph()
        graph.add_edge(1, 2)
        graph.add_edge(1, 4)
        graph.add_edge(3, 2)
        graph.add_edge(3, 4)
        
        set_0, set_1 = graph.get_partite_sets()
        self.assertEqual(len(set_0) + len(set_1), 4)
        self.assertTrue(
            (set_0 == {1, 3} and set_1 == {2, 4}) or 
            (set_0 == {2, 4} and set_1 == {1, 3})
        )

if __name__ == '__main__':
    unittest.main() 