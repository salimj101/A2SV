class Solution:
    def fib(self, n: int) -> int:
        memo = defaultdict(int)
        def ans(n):
            if n in memo:
                return memo[n]
            if n == 0:
                return 0
            if n == 1:
                return 1
            memo[n] = ans(n-1) + ans(n-2)
            
            return ans(n-1) + ans(n-2)

        return ans(n)

