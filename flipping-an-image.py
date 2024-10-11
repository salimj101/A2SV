class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        img=[list(reversed(i)) for i in image]
        val=[]
        for i in img:
            ans=[]
            for j in i:
                if j == 0:
                    ans.append(1)
                else:
                    ans.append(0) 
            val.append(ans)    
        return val