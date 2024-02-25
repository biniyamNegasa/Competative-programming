class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        count = defaultdict(list)
        for i,n in enumerate(nums):
            count[n].append((count[n][-1] if count[n] else 0)+i)
        ans = []
        dic = defaultdict(int)
        for i, n in enumerate(nums):
            sz = len(count[n])
            R = count[n][-1]-count[n][dic[n]]
            L = count[n][dic[n]]
            val = abs((dic[n]+1)*i - L)+abs(R-((sz-1-dic[n])*i))
            ans.append(val)
            dic[n]+=1
        return ans