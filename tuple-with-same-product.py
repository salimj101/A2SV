class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        product_count = Counter() 
        result = 0

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                product = nums[i] * nums[j]
                product_count[product] += 1

       
        for freq in product_count.values():
            if freq > 1:
                result += (freq * (freq - 1)) // 2 
        return result * 8 
        