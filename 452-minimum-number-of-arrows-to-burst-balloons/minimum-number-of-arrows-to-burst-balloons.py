class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        n = len(points)

        # sort based on the end points
        points.sort(key=lambda x: x[1])

        arrows = 1
        ending = points[0][1]

        for i in range(1, n):
            if points[i][0] <= ending <= points[i][1]:
                continue
            else:
                arrows += 1
                ending = points[i][1]
        
        return arrows
