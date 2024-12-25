class BipartiteGraph:
    def __init__(self):
        self.graph = {}
        self.colors = {}  # Store node colors (0 or 1)

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
            self.colors[vertex] = None

    def add_edge(self, v1, v2):
        if v1 not in self.graph:
            self.add_vertex(v1)
        if v2 not in self.graph:
            self.add_vertex(v2)
            
        self.graph[v1].append(v2)
        self.graph[v2].append(v1)

    def is_bipartite(self):
        # If graph is empty, it's bipartite
        if not self.graph:
            return True

        # Reset colors
        self.colors = {vertex: None for vertex in self.graph}
        
        # Check each unvisited vertex
        for vertex in self.graph:
            if self.colors[vertex] is None:
                # Start with color 0
                self.colors[vertex] = 0
                
                # If BFS returns False, graph is not bipartite
                if not self._bfs_color(vertex):
                    return False
        
        return True

    def _bfs_color(self, start_vertex):
        queue = [start_vertex]
        
        while queue:
            current = queue.pop(0)
            
            # Check all adjacent vertices
            for neighbor in self.graph[current]:
                # If neighbor hasn't been colored yet
                if self.colors[neighbor] is None:
                    # Color it with opposite color
                    self.colors[neighbor] = 1 - self.colors[current]
                    queue.append(neighbor)
                # If neighbor has same color as current vertex
                elif self.colors[neighbor] == self.colors[current]:
                    return False
                    
        return True

    def get_partite_sets(self):
        if not self.is_bipartite():
            return None
            
        set_0 = {v for v, color in self.colors.items() if color == 0}
        set_1 = {v for v, color in self.colors.items() if color == 1}
        
        return set_0, set_1 