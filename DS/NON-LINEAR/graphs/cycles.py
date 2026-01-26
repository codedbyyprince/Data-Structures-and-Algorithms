from collections import deque

# Building Graph 
def dict_graph(n , edges):
    graph = {}

    for i in range(n):
        graph[i] = []

    for u, v in edges:
        graph[u].append(v)
    
    return graph

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
