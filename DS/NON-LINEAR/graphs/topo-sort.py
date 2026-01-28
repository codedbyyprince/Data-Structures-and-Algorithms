from collections import deque

# directed graph 
def directed_graph(n, edges):
    graph = {i: [] for i in range(n)}

    for u, v in edges:
        graph[u].append(v)

    return graph


# topological sort
def topo_sort(graph, n):
    indegree = [0] * n

    for u in graph:
        for v in graph[u]:
            indegree[v] += 1

    q = deque()
    for i in range(n):
        if indegree[i] == 0:
            q.append(i)

    topo_order = []

    while q:
        node = q.popleft()
        topo_order.append(node)
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                q.append(neighbor)

    if len(topo_order) != n:
        print("Cycle Detected ")

    return topo_order

n = 4
edges = [
    (0, 1),
    (0, 2),
    (1, 3),
    (2, 3)
]


graph = directed_graph(n, edges)
print("Graph:", graph)

order = topo_sort(graph, n)
print("Topological Order:", order)
