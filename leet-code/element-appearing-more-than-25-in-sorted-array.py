class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        count=Counter(arr)
        check=len(arr)/4
        for num in count:
            if count[num]>check:
                return num