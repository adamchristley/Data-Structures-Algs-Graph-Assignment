class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)  # Assuming undirected graph

    def dfs_util(self, v, visited):
        visited.add(v)
        print(v, end=' ')

        for neighbor in self.graph[v]:
            if neighbor not in visited:
                self.dfs_util(neighbor, visited)

    def dfs(self, start_vertex):
        visited = set()
        self.dfs_util(start_vertex, visited)

    def bfs(self, start_vertex):
        visited = set()
        queue = [start_vertex]
        visited.add(start_vertex)

        while queue:
            v = queue.pop(0)
            print(v, end=' ')

            for neighbor in self.graph[v]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)

class TransportationNetwork:
    def __init__(self):
        self.graph = Graph()

    def add_city(self, city):
        self.graph.add_vertex(city)

    def add_road(self, city1, city2):
        self.graph.add_edge(city1, city2)

    def shortest_path(self, start_city, end_city):
        visited = set()
        queue = [(start_city, [start_city])]

        while queue:
            (city, path) = queue.pop(0)
            visited.add(city)

            if city == end_city:
                return path

            for neighbor in self.graph.graph[city]:
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))

        return "No path found"
graph = Graph()
graph.dfs()