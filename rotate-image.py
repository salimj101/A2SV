class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # matrix[:] = list(zip(*matrix[::-1]))
        for i in range(len(matrix)):
            for j in range(i+1,len(matrix[0])):
                t= matrix[i][j]
                matrix[i][j]= matrix[j][i]
                matrix[j][i]=t
        
        for i in matrix:
            i.reverse()