class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        dic = defaultdict(int)
        ans = 0
        for n in answers:
            dic[n+1]+=1
        for n in dic:
            ans += ceil(dic[n]/n)*n
        return ans