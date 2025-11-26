class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x : x[1])
        end =points[0][1]
        count = 1
        n = len(points)
        
        for left, right in points[1:]:
            if left > end or end > right:
                end = right
                count += 1
            
                
        return count
    
