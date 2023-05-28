class Graph:
    def __init__(self, n_vertices):
        self.n = n_vertices
        self.adj_list = []
        self.path = []

    def addEdge(self, u, v, w, name):
        self.adj_list.append([u, v, w, name])

    def display(self, dist):
        print("Distance from Source")
        for i in range(self.n):
            print(i,dist[i])
        print("Path is: " ,self.path)

    def BellmanFord(self, src):
        dist = [float("Inf")] * self.n
        dist[src] = 0

        for _ in range(self.n - 1):
            for u, v, w, name in self.adj_list:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    self.path.append(name)

        for u, v, w, name in self.adj_list:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                print("Graph contains negative weight cycle")
                return

        self.display(dist)

if __name__ == '__main__':
    g = Graph(8) 
    g.addEdge(1, 2, 6, "A")
    g.addEdge(1, 4, 5, "B")
    g.addEdge(1, 3, 5, "C")
    g.addEdge(3, 2, -2, "D")
    g.addEdge(4, 2, -2, "E")
    g.addEdge(2, 5, -1, "F")
    g.addEdge(3, 5, 1, "G")
    g.addEdge(4, 6, -1, "H")
    g.addEdge(5, 7, 3, "I")
    g.addEdge(6, 7, 3, "J")
    g.BellmanFord(1)
