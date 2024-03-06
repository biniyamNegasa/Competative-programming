class Solution:
    def bs(self, arr, start, end, target):
        left = start
        right = end
        while left<=right:
            mid = (left+right)//2
            if arr[mid][0]==target:
                return mid
            elif arr[mid][0]>target:
                right = mid -1
            else:
                left = mid+1
        return left if left<=end else -1
            

    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        dic = {a[0]:i for i,a in enumerate(intervals)}
        intervals.sort()
        n = len(intervals)
        ans = [0]*n

        for i,nums in enumerate(intervals):
            val = self.bs(intervals, i,n-1,nums[1])
            if val==-1:
                ans[dic[nums[0]]] = -1
            else:
                ans[dic[nums[0]]] = dic[intervals[val][0]]
        return ans