def diameter(root):
    ans = 0

    def dfs(node):
        nonlocal ans
        if not node:
            return 0
        left = dfs(node.left)
        right = dfs(node.right)
        ans = max(left, right)
        return max(left, right) + 1

    dfs(root)
    return ans
