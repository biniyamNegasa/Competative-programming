class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        s=set()
        for i,n in enumerate(fronts):
            if n==backs[i]:
                s.add(n)
        a=0
        b=0
        for n in sorted(fronts):
            if n not in s:
                a=n
                break
        for n in sorted(backs):
            if n not in s:
                b=n
                break
        return min(a, b) if a!=0 and b!=0 else max(a, b)