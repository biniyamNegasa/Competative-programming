class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        val = abs(target[0])+abs(target[1])
        for x,y in ghosts:
            checker = abs(x-target[0])+abs(y-target[1])
            if checker<=val:
                return False
        return True