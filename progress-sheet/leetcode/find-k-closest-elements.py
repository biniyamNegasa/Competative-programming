class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = 0
        right = len(arr)-1-k
        while left<=right:
            mid = (left+right)//2
            if x-arr[mid]>arr[mid+k]-x:
                left = mid+1
            else:
                right = mid-1
        return arr[left:left+k]