class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        num= [str(i) for i in nums]
        num.sort(reverse=True)
        if num[-1] == num[0] and num[0] == "0":
            return "0"
        else:
            for j in range(len(num)):
                for i in range(1,len(num)):
                    if len(num[i-1]) != len(num[i]) and num[i-1][0] == num[i][0]:
                        if num[i] + num[i-1] > num[i-1] + num[i]:
                            num[i],num[i-1] = num[i-1],num[i]        
            return "".join(num)