class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        start = points[0][0]
        end = points[0][1]
        ans = 1
        points.sort()
        for a, b in points:
            if a>end:
                ans+=1
                start = a
                end = b
            start = max(a,start)
            end = min(b, end)
        return ans