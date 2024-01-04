class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        check=skill[0]+skill[-1]
        ssum=0
        L=0
        R=len(skill)-1
        while L<R:
            if skill[L]+skill[R]!=check:
                return -1
            ssum += skill[L]*skill[R]
            L+=1
            R-=1
        return ssum