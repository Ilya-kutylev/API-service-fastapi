from collections import deque


def get_shortest_path(grid):
    def is_valid_more(x, y):
        return 0 <= x < n and 0 <= y < n and grid[x][y] == 0

    n = len(grid)
    if grid[0][0] != 0 or grid[n-1][n-1] != 0:
        return -1

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1,-1), (1, 1)]
    queue = deque([(0, 0, 1)])
    grid[0][0] = 1

    while queue:
        x, y, length = queue.popleft()

        if x == n-1 and y == n-1:
            return length

        for dx, dy in directions:
            nx, ny = dx + x, dy + y
            if is_valid_more(nx, ny):
                queue.append((nx, ny, length + 1))
                grid[nx][ny] = 1

    return -1

matrix = [
    [0, 0, 1],
    [1, 0, 1],
    [1, 0, 0]
]
result = get_shortest_path(matrix)
print(result)
