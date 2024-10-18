class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        R= len(matrix)
        C= len(matrix[0])
        direction= [(0,1),(1,0),(0,-1),(-1,0)]
        r,c,d= 0,0,0
        ans=[]
        visited= set()
        
        def bound(n_r,n_c):
            return 0<= n_r < R and 0<= n_c < C
        
        for i in range(R*C):
            ans.append(matrix[r][c])
            n_r, n_c= r+ direction[d][0], c+ direction[d][1]
            visited.add((r,c))

            if not bound(n_r,n_c) or (n_r,n_c) in visited:
                d= (d+1)% 4
                n_r,n_c= r+ direction[d][0], c+ direction[d][1]
            r,c= n_r,n_c

        return ans