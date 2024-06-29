class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        count = 0

        def island(i, j):
            if i >= m or i < 0 or j >= n or j < 0 or grid[i][j] == "0":
                return
            grid[i][j] = "0"
            island(i + 1, j)
            island(i - 1, j)
            island(i, j + 1)
            island(i, j - 1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    count += 1
                    island(i, j)
        return count
