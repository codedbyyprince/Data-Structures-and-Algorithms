from collections import deque

# undirected graph 
def undirected_graph(n, edges):
    graph = {i: [] for i in range(n)}

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    return graph

# conuting connected components
def counting_connected_components(n, graph):
    visited = [False] * n
    components = 0 

    for node in range(n):
        if not visited[node]:
            components += 1
            q = deque()
            q.append(node)
            visited[node] = True
        
        while q:
            current = q.popleft()
            for neighbor in graph[current]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    q.append(neighbor)
    return components

# example
n = 6
edges = [
    (0, 1),
    (1, 2),
    (3, 4)
]

graph = undirected_graph(n, edges)

print(graph)
print("Connected Components:", counting_connected_components(n, graph))
