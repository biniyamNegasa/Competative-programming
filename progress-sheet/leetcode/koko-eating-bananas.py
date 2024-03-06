class Solution:
    def countHour(self, arr, capacity):
        count = 0
        for n in arr:
            count += ceil(n/capacity)
        return count
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left<=right:
            mid = (left+right)//2
            this_hour = self.countHour(piles, mid)
            if this_hour>h:
                left = mid + 1
            else:
                right = mid - 1
        return left