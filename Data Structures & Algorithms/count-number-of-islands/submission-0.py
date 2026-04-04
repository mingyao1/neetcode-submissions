class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0      
        row, col = len(grid), len(grid[0])
        visited = set()     
        islands = 0

        def bfs(r, c):
            queue = deque()
            queue.append((r, c))
            
            while queue:
                r, c = queue.popleft()

                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    new_r = r + dr
                    new_c = c + dc

                    if new_r in range(row) and new_c in range(col) and (new_r, new_c) not in visited and grid[new_r][new_c] == "1":
                        queue.append((new_r, new_c))
                        visited.add((new_r, new_c))




        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1" and (r, c) not in visited:
      
                    visited.add((r, c))

                    bfs(r, c)
                    islands += 1


        return islands
