class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans = list(s)
        for i in spaces:
            ans[i] = ' ' + ans[i]
        return ''.join(ans)