class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack = []
        
        for num in nums:
            while stack and math.gcd(stack[-1], num) > 1:
                num = (stack[-1] * num) // math.gcd(stack[-1], num)  # LCM
                stack.pop()
            stack.append(num)
        
        return stack