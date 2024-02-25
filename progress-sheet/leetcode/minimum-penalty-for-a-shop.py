class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        no_arr, yes_arr = [0]*n, [0]*n
        for i, customer in enumerate(customers):
            if customer=='Y':
                yes_arr[i] = 1
            else:
                no_arr[i] = 1
        yes_arr.reverse()
        yes_ps, no_ps = [0], [0]
        for val in no_arr:
            no_ps.append(no_ps[-1]+val)
        for val in yes_arr:
            yes_ps.append(yes_ps[-1]+val)
        yes_ps.reverse()
        mn = -1
        mn_val = 3*n
        for i, val in enumerate(yes_ps):
            penality = val+no_ps[i]
            if penality<mn_val:
                mn_val = penality
                mn = i
        return mn