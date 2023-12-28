from math import inf
from heapq import *

distances = [inf] * n
distances[source] = 0
heap = [(0, source)]

while heap:
    curr_dist, node = heapop(heap)
    if curr_dist > distances[node]:
        continue

    for next_node, weight in graph[node]:
        dist = curr_dist + weight
        if dist < distances[next_node]:
            distances[next_node] = dist
            heappush(heap, (dist, next_node))
