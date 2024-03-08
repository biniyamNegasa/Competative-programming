class Solution:
    def numberOfWays(self, s: str) -> int:
        ps0 = [0]
        ps1 = [0]
        ps01 = [0]
        ps10 = [0]
        ps101 = [0]
        ps010 = [0]
        for ch in s:
            if ch=='0':
                ps0.append(ps0[-1]+1)
                ps1.append(ps1[-1])
            else:
                ps1.append(ps1[-1]+1)
                ps0.append(ps0[-1])
        for i, ch in enumerate(s):
            if ch=='0':
                ps01.append(ps01[-1])
                ps10.append(ps10[-1]+ps1[i])
            else:
                ps10.append(ps10[-1])
                ps01.append(ps01[-1]+ps0[i])
        for i, ch in enumerate(s):
            if ch=='0':
                ps101.append(ps101[-1])
                ps010.append(ps010[-1]+ps01[i])
            else:
                ps010.append(ps010[-1])
                ps101.append(ps101[-1]+ps10[i])
        return ps010[-1]+ps101[-1]