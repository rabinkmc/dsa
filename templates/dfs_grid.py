def dfs(grid, i, j):
    m = len(grid)
    n = len(grid[0])
    stack = [(i, j)]
    while stack:
        r, c = stack.pop()
        # logic
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            rr, cc = r + dr, c + dc
            if rr < 0 or rr >= m or cc < 0 or cc >= n or grid[rr][cc] == 0:
                continue
            stack.append((rr, cc))
