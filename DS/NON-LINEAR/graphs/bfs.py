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

def bfs(adj, src):
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

V = 6
edges = [
    [0,1],[0,2],[0,4],[0,5],
    [1,3],[1,5],[1,2],
    [2,4],[2,5],
    [3,4],[3,5],
    [4,1],[5,4]
]

adj = dict_graph(V, edges)

print(adj)