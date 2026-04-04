class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        M, N = len(obstacleGrid), len(obstacleGrid[0])

        dp = {(M - 1, N - 1): 1}

        def dfs(m, n):
            if m == M or n == N or obstacleGrid[m][n] == 1:
                return 0
            
            if (m, n) in dp:
                return dp[(m, n)]
            
            dp[(m, n)] = dfs(m + 1, n) + dfs(m, n + 1)

            return dp[(m, n)]

        return dfs(0, 0)


            