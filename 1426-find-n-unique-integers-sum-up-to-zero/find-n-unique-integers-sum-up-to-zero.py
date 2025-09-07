class Solution:
    def sumZero(self, n: int) -> List[int]:
        k=[]
        if n % 2 != 0:
            k.append(0)

        for i in range(1,n//2+1):
            k.append(i)
            k.append(-i)

        return k