def adjacency_list_undirected(V, edges):
    adjacency_list = {}

    for i in range(V):
        adjacency_list[i] = []

    for u, v in edges:
        adjacency_list[u].append(v)
        adjacency_list[v].append(u)

    for vertex in adjacency_list:
        print(vertex, "->", adjacency_list[vertex])

V = 6
edges = [
    [0,1],[0,2],[0,4],[0,5],
    [1,3],[1,5],[1,2],
    [2,4],[2,5],
    [3,4],[3,5],
    [4,3],[4,1],
    [5,3],[5,4]
]

adjacency_list_undirected(V, edges)ohk t