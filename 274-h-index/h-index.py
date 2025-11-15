class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        low = 0
        hight = len(citations)
        
        def target(mid):
            # how many papers are cited h(mid) times
            count = 0
            for i in citations:
                if i >= mid:
                    count += 1
                    
            return count >= mid
            
        while low <= hight:
            mid =  low + (hight - low) // 2
            
            if target(mid):
                low = mid + 1
            else:
                hight = mid - 1
                
        return hight
            