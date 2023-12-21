class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        cur_max = max(candies)
        ans = []
        for num in candies:
            if num+extraCandies>=cur_max:
                ans.append(True)
            else:
                ans.append(False)
        return ans