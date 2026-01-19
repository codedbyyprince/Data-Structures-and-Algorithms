from collections import deque


# Building Graph 
def dict_graph(V , edges):
    adj = {}

    for i in range(V):
        adj[i] = []

    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    return adj
# BFS 

# Connected 
def Connected_bfs(adj, src):
    visited = set()
    q = deque()
    res = []
    
    visited.add(src)
    q.append(src)

    while q:
        curr = q.popleft()
        res.append(curr)

        for neighbor in adj[curr]:
            if neighbor not in visited:
                visited.add(neighbor)
                q.append(neighbor)
    
    return res

# Disconnected func

# Helper
def bfs_from_node(adj, src , res , visited):
    q = deque()

    visited.add(src)
    q.append(src)

    while q:
        curr = q.popleft()
        res.append(curr)

        for neighbour in adj[curr]:
            if neighbour not in visited:
                visited.add(neighbour)
                q.append(neighbour)
    
# Disconnected
def  bfs_disconnected(adj):
    visited = set()
    res = []

    for node in adj:
        if node not in visited:
            bfs_from_node(adj, node, res, visited)
    
    return res


# Example run

V = 6
edges = [
    [0,1],[0,2],[0,3],
    [1,2],[1,3],
    [2,3],

    [4,5]
]


adj = dict_graph(V, edges)

print(f'Graph = {adj}')

print(f'Connected BFS = {Connected_bfs(adj, 0)}')

print(f'Disconnected BFS = {bfs_disconnected(adj)}')
