class Solution:
    def countDay(self, arr, capacity):
        days = 1
        tot = 0
        for n in arr:
            tot+=n
            if tot>capacity:
                days+=1
                tot = n
        return days


    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)

        while left<=right:
            mid = (left+right)//2
            this_day = self.countDay(weights, mid)
            if this_day>days:
                left = mid + 1
            else:
                right = mid-1
        return left