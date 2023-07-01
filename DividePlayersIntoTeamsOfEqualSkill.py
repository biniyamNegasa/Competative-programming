class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        left=0
        right=len(skill)-1
        sum=0
        t=skill[0]+skill[-1]
        while left<right:
            if skill[left]+skill[right] != t:
                return -1
            sum+=skill[left]*skill[right]
            left+=1
            right-=1
        return sum
