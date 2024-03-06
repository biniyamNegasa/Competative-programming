class Solution:
    def prev(self, arr, target):
        left = 0
        right = len(arr)-1
        while left<=right:
            mid = (left+right)//2
            if arr[mid]>=target:
                right = mid-1
            else:
                left = mid+1
        return arr[left] if -1<left<len(arr) else arr[0]
    
    def next(self, arr, target):
        left = 0
        right = len(arr)-1
        while left<=right:
            mid = (left+right)//2
            if arr[mid]>target:
                right = mid-1
            else:
                left = mid+1
        return arr[right] if -1<right<len(arr) else arr[-1]
    
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        ans = []
        for house in houses:
            p = self.prev(heaters, house)
            n = self.next(heaters, house)
            ans.append(min(abs(house-p), abs(house-n)))
        return max(ans)