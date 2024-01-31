from collections import defaultdict

def topological_sort(graph: dict[str, list[str]]) -> list[str]:
    """
    Topological sort for a network of nodes

        graph = {"A": ["B", "C"], "B": [], "C": ["B"]}
        topological_sort(graph)
        # ["A", "C", "B"]

    :param nodes: Nodes of the network
    :return: nodes in topological order
    """

    # Calculate the indegree for each node
    indegrees = defaultdict(int)
    for node in graph:
        for dependency in graph[node]:
            indegrees[dependency] += 1

    # Place all elements with indegree 0 in queue
    queue = [k for k in graph if indegrees[k] == 0]

    final_order = []

    # Continue until all nodes have been dealt with
    while queue:
        node = queue.pop()
        final_order.append(node)

        for dependency in graph[node]:
            indegrees[dependency] -= 1
            if indegrees[dependency] == 0:
                queue.append(dependency)


    # check for circular dependencies
    if len(final_order) != len(graph):
        raise Exception("Circular dependency found.")

    return final_order


graph = {"A": ["B", "C"], "B": [], "C": ["B"]}
print(topological_sort(graph))
