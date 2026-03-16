import heapq

def undirected_graph(n, edges):
    graph = [[] for _ in range(n)]
    for u, v, w in edges:
       graph[u].append(v, w)
       graph[v].append(u, w)

    return graph

def dijkstra(graph, start):

    n = len(graph)
    dist = [float('inf')] * n
    dist[start] = 0

    pq = []
    heapq.heappush(pq, (0, start))

    while pq:

        curr_dist, node = heapq.heappop(pq)

        if curr_dist > dist[node]:
            continue

        for neighbor, weight in graph[node]:

            new_dist = curr_dist + weight

            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))

    return dist