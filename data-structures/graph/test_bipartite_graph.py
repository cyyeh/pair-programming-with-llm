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

    def test_disconnected_components(self):
        graph = BipartiteGraph()
        # First component
        graph.add_edge(1, 2)
        graph.add_edge(2, 3)
        # Second component
        graph.add_edge(4, 5)
        graph.add_edge(5, 6)
        self.assertTrue(graph.is_bipartite())

    def test_single_vertex(self):
        graph = BipartiteGraph()
        graph.add_vertex(1)
        self.assertTrue(graph.is_bipartite())
        set_0, set_1 = graph.get_partite_sets()
        self.assertTrue(1 in set_0 or 1 in set_1)

    def test_complex_bipartite(self):
        graph = BipartiteGraph()
        # Create a more complex bipartite graph
        # Left set: 1, 3, 5
        # Right set: 2, 4, 6
        graph.add_edge(1, 2)
        graph.add_edge(1, 4)
        graph.add_edge(1, 6)
        graph.add_edge(3, 2)
        graph.add_edge(3, 4)
        graph.add_edge(5, 2)
        graph.add_edge(5, 6)
        self.assertTrue(graph.is_bipartite())
        set_0, set_1 = graph.get_partite_sets()
        self.assertEqual(len(set_0) + len(set_1), 6)

    def test_odd_cycle_not_bipartite(self):
        graph = BipartiteGraph()
        # Create a pentagon (cycle of length 5)
        graph.add_edge(1, 2)
        graph.add_edge(2, 3)
        graph.add_edge(3, 4)
        graph.add_edge(4, 5)
        graph.add_edge(5, 1)
        self.assertFalse(graph.is_bipartite())

    def test_partite_sets_none_for_non_bipartite(self):
        graph = BipartiteGraph()
        # Create a triangle
        graph.add_edge(1, 2)
        graph.add_edge(2, 3)
        graph.add_edge(3, 1)
        self.assertIsNone(graph.get_partite_sets())

    def test_add_same_edge_twice(self):
        graph = BipartiteGraph()
        graph.add_edge(1, 2)
        graph.add_edge(1, 2)  # Adding same edge again
        self.assertTrue(graph.is_bipartite())
        set_0, set_1 = graph.get_partite_sets()
        self.assertEqual(len(set_0) + len(set_1), 2)

if __name__ == '__main__':
    unittest.main() 