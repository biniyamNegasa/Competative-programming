class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def comp(x, y):
            if x+y>y+x:
                return -1
            return 1
        return str(int(''.join(sorted([str(n) for n in nums], key=cmp_to_key(comp)))))