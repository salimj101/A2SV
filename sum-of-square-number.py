class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left, right = 0, int(sqrt(c))

        while left <= right:
            sum_squares = left * left + right * right
            if sum_squares == c:
                return True
            elif sum_squares > c:
                right -= 1
            else:
                left += 1
        
        return False

        
        