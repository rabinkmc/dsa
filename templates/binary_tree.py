from collections import deque


def fn(root):
    queue = deque([root])
    ans = 0

    while queue:
        current_length = len(queue)
        ans = 0
        for _ in range(current_length):
            node = queue.popleft()
            # do logic:
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return ans
