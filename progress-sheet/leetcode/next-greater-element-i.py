class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic = defaultdict(lambda: -1)
        stk = []
        for n in nums2:
            while stk and stk[-1]<n:
                dic[stk.pop()] = n
            stk.append(n)
        for n in nums1:
            yield dic[n]