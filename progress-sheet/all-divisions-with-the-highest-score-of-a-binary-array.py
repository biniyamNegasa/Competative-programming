class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        one_ps = [0]
        zero_ps = [0]
        for n in nums:
            if n:
                one_ps.append(n+one_ps[-1])
                zero_ps.append(zero_ps[-1])
            else:
                one_ps.append(one_ps[-1])
                zero_ps.append(1+zero_ps[-1])
        dic = defaultdict(list)
        for i in range(len(nums)+1):
            dic[(one_ps[-1]-one_ps[i]+zero_ps[i])].append(i)
        return dic[max(dic)]