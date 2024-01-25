class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        dic_f = {}
        dic_b = {}
        n = len(nums)
        for i in range(n):
            if nums[i]<0:
                dic_f[i] = (i+nums[i])%n
            else:
                dic_b[i] = (i+nums[i])%n
        lst = list(dic_f)
        alst = list(dic_b)
        ans1 = False
        ans2 = False
        for i in lst:
            f = i
            l = dic_f[f]
            while l in dic_f and dic_f[l] in dic_f and l!=dic_f[l]:
                if f == l:
                    ans1 = True
                    break
                f = dic_f[f]
                l = dic_f[dic_f[l]]
                    
        for i in alst:
            f = i
            l = dic_b[f]
            while l in dic_b and dic_b[l] in dic_b and l!=dic_b[l]:
                if f == l:
                    ans2 = True
                    break
                f = dic_b[f]
                l = dic_b[dic_b[l]]
        return ans1 or ans2