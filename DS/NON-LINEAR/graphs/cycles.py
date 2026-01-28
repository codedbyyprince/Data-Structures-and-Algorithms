from collections import deque

# Directed Graph 
def directed_graph(n , edges):
    graph = {}

    for i in range(n):
        graph[i] = []

    for u, v in edges:
        graph[u].append(v)
    
    return graph

# Cycle Directed
def cycle_directed(graph , n):
    indegree = {}
    for i in range(n):
        indegree[i] = 0

    for node in graph:
        for neighbour in graph[node]:
            indegree[neighbour] += 1

    q = deque()
    
    for node in indegree:
        if indegree[node] == 0:
            q.append(node)
    count = 0

    while q:
        current = q.popleft()
        count = count + 1 

        for neighbour in graph[current]:
            indegree[neighbour] = indegree[neighbour] - 1
            if indegree[current] == 0:
                q.append(neighbour)

    if count == n:
        return False
    else:
        return True

# Undirected Graph
def undirected_graph(V, edges):
    graph = {i: [] for i in range(V)}

    for u, v in edges:
        u.append(v)
        v.append(u)
    return graph

# Cycle Undirected
def cycle_undirected(graph , V):
    visited = V * [False]

    def dfs(node, parent):
        visited[node] = True

        for neighbour in graph[node]:
            if not visited[neighbour]:
                if dfs(neighbour, node):
                    True
                elif neighbour != parent:
                    True
        return False

    for i in range(V):
        if not visited[i]:
            if dfs(i, -1):
                return True
    
    return False

V = 6
edges = [
    [0,1],[0,2],[0,4],[0,5],
    [1,3],[1,5],[1,2],
    [2,4],[2,5],
    [3,4],[3,5],
    [4,3],[4,1],
    [5,3],[5,4]
]

V = 6
edges2 = [
    [0,1],
    [1,2],
    [2,3],
    [3,4],
    [4,5]
]


graph = directed_graph(V , edges)
print(cycle_directed(graph, V))

graph = directed_graph(V , edges2)
print(cycle_directed(graph, V))