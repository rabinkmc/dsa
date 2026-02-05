from math import inf
from heapq import heappush, heappop

def next_candidates(node):
    # implement your node
    return node

def dijkstra(source, end):
    distances = dict()
    # initialize all the distances of node to inf
    distances[source] = 0 # set source distance to 0
    heap = [(source, 0)] # push the source node
    while heap:
        node, curr_dist = heappop(heap) # process the node
        if curr_dist > distances[node]:
            continue
        for next_node, weight in next_candidates(node):
            dist = curr_dist + weight
            if dist < distances[next_node]:
                distances[next_node] = dist
                heappush(heap, (next_node, dist))
    return distances[end]
