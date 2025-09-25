class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)      
        memo = {}  
        def dp(i , j):

            if i == n or j == m:
                return 0

            if (i,j) in memo:
                return memo[(i,j)]
            # take
            take = not_take1 = not_take2 = 0 
            if text1[i] == text2[j]:
                take = 1 + dp(i + 1 , j + 1)
            else:
                not_take1 = dp(i , j + 1)
                not_take2 = dp(i + 1 , j)
            

            memo[(i,j)] = max(take , not_take1 , not_take2)
            return memo[(i,j)]


        return dp(0 , 0)