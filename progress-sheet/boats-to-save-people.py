class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        c=0
        L=0
        R=len(people)-1
        while L<=R:
            if people[L]+people[R]<=limit:
                L+=1
            c+=1
            R-=1
        return c