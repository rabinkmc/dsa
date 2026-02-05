graph = {"A": {"B": 4, "C": 2}, "B": {"C": 5, "D": 10}, "C": {"D": 3}, "D": {}}

import heapq


def dijkstra(graph, source):
    dist = {}
    for node in graph:
        dist[node] = float("inf")
    dist[source] = 0
    pq = [(0, source)]
    while pq:
        curr_dist, node = heapq.heappop(pq)
        if curr_dist > dist[node]:
            continue

        for adj in graph[node]:
            new_dist = curr_dist + graph[node][adj]
            if dist[adj] > new_dist:
                dist[adj] = new_dist
                heapq.heappush(pq, (new_dist, adj))
    return dist


print(dijkstra(graph, "A"))
