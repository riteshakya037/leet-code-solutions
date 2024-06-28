class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        
        def bfs(queue: List[Tuple[int, int]]) -> Set[Tuple[int, int]]:
            visited = {(ii, jj) for (ii, jj) in queue}
            while queue:
                row, col = queue.popleft()
                for uu, vv in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
                    if 0 <= uu < m and 0 <= vv < n and (uu, vv) not in visited and heights[uu][vv] >= heights[row][col]:
                        # Visit uu, vv
                        visited.add((uu, vv))
                        queue.append((uu, vv))
            return visited
        
        # Add pacific nodes
        pacific_queue = collections.deque()
        for jj in range(n):
            pacific_queue.append((0, jj))
        for ii in range(1, m):
            pacific_queue.append((ii, 0))
        
        # Add atlantic nodes
        atlantic_queue = collections.deque()
        for jj in range(n):
            atlantic_queue.append((m - 1, jj))
        for ii in range(0, m - 1):
            atlantic_queue.append((ii, n - 1))
        
        pacific = bfs(pacific_queue)
        atlantic = bfs(atlantic_queue)
        return pacific.intersection(atlantic)
