def hamilton(graph):
    n = len(graph)
    path = [-1] * n
    def isvalid(vertex, pos):
        if graph[path[pos-1]][vertex] == 0:
            return False
        for i in range(pos):
            if path[i] == vertex:
                return False
        return True
    def findcircuit(pos):
        if pos == n:
            if graph[path[pos-1]][path[0]] == 1:
                return True
            else:
                return False
        for vertex in range(1, n):
            if isvalid(vertex, pos):
                path[pos] = vertex
                if findcircuit(pos + 1):
                    return True
                path[pos] = -1
        return False
    path[0] = 0
    if findcircuit(1):
        return path
    else:
        return None
graph = [[0, 1, 1, 1],
         [1, 0, 1, 0],
         [1, 1, 0, 1],
         [1, 0, 1, 0]]

path = hamilton(graph)
if path is not None:
    print("Hamiltonian Circuit found: ", end="")
    for vertex in path:
        print(vertex, end=" ")
else:
    print("No Hamiltonian Circuit found.")

