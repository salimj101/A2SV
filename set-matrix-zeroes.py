class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero=[]
        for col in range(len(matrix)):
            for row in range(len(matrix[0])):
                if matrix[col][row] == 0:
                    zero.append([col,row])
        
        for col,row in zero:
            for r in range(len(matrix[0])):
                matrix[col][r] = 0
            for c in range(len(matrix)):
                matrix[c][row] = 0
        return zero
                
