class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        maxLocal = []

        for i in range(n - 2):
            maxLocal_row = []
            for j in range(n - 2):
                submatrix = [grid[i + k][j:j + 3] for k in range(3)]
                max_value = max(max(submatrix, key=lambda x: max(x)))
                maxLocal_row.append(max_value)
            maxLocal.append(maxLocal_row)

        return maxLocal
