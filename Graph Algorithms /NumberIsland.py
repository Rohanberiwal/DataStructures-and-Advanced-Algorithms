class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = [[False] * cols for _ in range(rows)]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(row, col):
            if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == '0' or visited[row][col]:
                return
            visited[row][col] = True
            for dr, dc in directions:
                dfs(row + dr, col + dc)

        num_islands = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1' and not visited[i][j]:
                    dfs(i, j)
                    num_islands += 1

        return num_islands
            
