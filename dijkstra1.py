from collections import deque
# graph
# visit the smallest node
# go to its nearest neighbors
#

graph = {}
graph["start"] = {}
graph["start"]["a"] = 5
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["c"] = 4
graph["a"]["d"] = 2

graph["b"] = {}
graph["b"]["a"] = 8
graph["b"]["d"] = 7

graph["c"] = {}
graph["c"]["finish"] = 3
graph["c"]["d"] = 6

graph["d"] = {}
graph["d"]["finish"] = 1
graph["finish"] = {}

inf = float("inf")
costs = {}
costs["a"] = 5
costs["b"] = 2
costs["c"] = inf
costs["d"] = inf
costs["finish"] = inf

parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["c"] = None
parents["d"] = None
parents["finish"] = None


processed = []


def find_lowest_cost_node(costs):
    print(costs)
    lowest_cost_node = None
    lowest_cost = float("inf")
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if new_cost < costs[n]:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)

path = deque()
key = "finish"
while key != "start":
    path.appendleft(key)
    key = parents[key]
path.appendleft("start")
