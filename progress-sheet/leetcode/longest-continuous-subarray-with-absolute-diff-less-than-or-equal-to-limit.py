class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        mx = 0
        mn_q, mx_q = Deque(), Deque()
        L = 0
        for R, n in enumerate(nums):
            while mn_q and n<mn_q[-1]:
                mn_q.pop()
            mn_q.append(n)
            while mx_q and n>mx_q[-1]:
                mx_q.pop()
            mx_q.append(n)
            while mn_q and mx_q and mx_q[0]-mn_q[0]>limit:
                if nums[L]==mn_q[0]:
                    mn_q.popleft()
                if nums[L]==mx_q[0]:
                    mx_q.popleft()
                L+=1
            mx = max(mx, R-L+1)
        return mx