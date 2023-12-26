class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ans=0
        for i in range(1,len(points)):
            x1=points[i-1][0]
            y1=points[i-1][1]
            x2=points[i][0]
            y2=points[i][1]
            ans += max(abs(x2-x1), abs(y2-y1))
        return ans