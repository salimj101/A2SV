class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        rows, cols = len(matrix), len(matrix[0])
        dp = [[0] * cols for _ in range(rows)]  
        directions = [(0,1), (1,0), (-1,0), (0,-1)]

        def dfs(i, j):
            if dp[i][j]: 
                return dp[i][j]

            max_length = 1  

            for dx, dy in directions:
                ni, nj = i + dx, j + dy
                if 0 <= ni < rows and 0 <= nj < cols and matrix[ni][nj] > matrix[i][j]:
                    max_length = max(max_length, 1 + dfs(ni, nj))

            dp[i][j] = max_length
            return dp[i][j]

        result = 0
        for i in range(rows):
            for j in range(cols):
                result = max(result, dfs(i, j))

        return result