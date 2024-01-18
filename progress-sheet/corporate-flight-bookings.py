class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        pre_sum = [0]*(n+1)
        for a,b,val in bookings:
            pre_sum[a-1]+=val
            pre_sum[b]-=val
        ans = []
        cur = 0
        for i in range(n):
            cur += pre_sum[i]
            ans.append(cur)
        return ans