from collections import defaultdict
from heapq import heappop, heappush


def dijkstra(graph, source):
    dist = {node: float("inf") for node in graph}
    pq = [(0, source)]
    dist[source] = 0
    parent = {
        source: None,
    }
    while pq:
        cdist, node = heappop(pq)
        if dist[node] < cdist:
            continue
        for adj in graph[node]:
            new_dist = graph[node][adj] + cdist
            if new_dist < dist[adj]:
                dist[adj] = new_dist
                heappush(pq, (new_dist, adj))
                parent[adj] = node
    return dist, parent


def build_graph(graph):
    result = defaultdict(dict)
    for u, v, w in graph:
        result[u][v] = w
        if v not in result:
            result[v] = {}
    return result


weighted_graph = [
    ("A", "B", 4),
    ("A", "C", 2),
    ("B", "C", 5),
    ("B", "D", 10),
    ("C", "E", 3),
    ("E", "D", 4),
    ("D", "F", 11),
    ("E", "F", 5),
]


def bellman_ford(weighted_graph, source):
    vertices = set()
    for u, v, _ in weighted_graph:
        vertices.add(u)
        vertices.add(v)
    v = len(vertices)
    dist = defaultdict(lambda: float("inf"))
    dist[source] = 0
    for _ in range(v - 1):
        for u, v, w in weighted_graph:
            new_dist = dist[u] + w
            if new_dist < dist[v]:
                dist[v] = new_dist
    return dist


indexed_graph = [
    (0, 1, 4),
    (0, 2, 2),
    (1, 2, 5),
    (1, 3, 10),
    (2, 4, 3),
    (4, 3, 4),
    (3, 5, 11),
    (4, 5, 5),
]


def floyd_warshall(edges):
    vertices = set()
    for u, v, _ in edges:
        vertices.add(u)
        vertices.add(v)
    V = len(vertices)
    dist = [[float("inf")] * V for _ in range(V)]
    for i in range(V):
        dist[i][i] = 0
    for u, v, w in edges:
        dist[u][v] = w
    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist


graph = build_graph(weighted_graph)
# print(dijkstra(graph, "A"))
# print(bellman_ford(weighted_graph, "A"))
print(floyd_warshall(indexed_graph))
