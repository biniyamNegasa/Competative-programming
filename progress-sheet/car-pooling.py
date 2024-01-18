class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        mx = max(trips, key= lambda x : x[2])[2]
        pre_sum = [0]*(mx+1)
        for n_psgrs, frm, to in trips:
            pre_sum[frm]+=n_psgrs
            pre_sum[to]-=n_psgrs
        curr = 0
        for n in pre_sum:
            curr+=n
            if curr>capacity:
                return False
        return True