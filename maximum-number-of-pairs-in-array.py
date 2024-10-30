class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        num=Counter(nums)
        ans=0
        leftover=0
        print(num)
        for val,freq in num.items():
            if freq % 2 == 0:
                ans = ans+ (freq//2)
            elif freq > 2:
                ans= ans+ ((freq-1)//2)
                leftover+=1
            else:
                leftover+=1
        return ans,leftover        