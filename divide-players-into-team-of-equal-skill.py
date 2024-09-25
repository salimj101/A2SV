class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        
        skill.sort()
        left,right = 0, len(skill) -1
        ans=[]
        val=[]
        while left < right:
            ans.append(skill[left] * skill[right])
            val.append(skill[left] + skill[right])
            left+=1
            right-=1
        
        for i in range(1,len(val)):
            if val[i-1] != val[i]:
                return -1
        return sum(ans)