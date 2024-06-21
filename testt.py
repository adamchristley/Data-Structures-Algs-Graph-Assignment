class Graph:

    def __init__(self):

        self.vertices = {}

    def add_vertex(self, vertex):

        if vertex not in self.vertices:
            self.vertices[vertex] = []

    def add_edge(self, v1, v2):

        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].append(v2)

            self.vertices[v2].append(v1)

    def depth_first_search(self, start_vertex, visited=None):

        if visited is None:
            visited = set()

        visited.add(start_vertex)

        print(start_vertex)

        for neighbor in self.vertices[start_vertex]:

            if neighbor not in visited:
                self.depth_first_search(neighbor, visited)

    def breadth_first_search(self, start_vertex):

        visited = set()

        queue = [start_vertex]

        visited.add(start_vertex)

        while queue:

            current_vertex = queue.pop(0)

            print(current_vertex)

            for neighbor in self.vertices[current_vertex]:

                if neighbor not in visited:
                    visited.add(neighbor)

                    queue.append(neighbor)


# Sample Usage of Graph

graph = Graph()

graph.add_vertex("A")

graph.add_vertex("B")

graph.add_vertex("C")

graph.add_vertex("D")

graph.add_vertex("E")

graph.add_edge("A", "B")

graph.add_edge("A", "C")

graph.add_edge("B", "D")

graph.add_edge("C", "E")

print("Depth-First Search:")

graph.depth_first_search("A")

print("\nBreadth-First Search:")

graph.breadth_first_search("A")