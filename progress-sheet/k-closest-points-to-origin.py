class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dic=defaultdict(list)
        for n in points:
            dic[tuple(n)].append(n[0]**2 + n[1]**2)
        ans = []
        for n in sorted(dic, key= lambda x: dic[x]):
            c=len(dic[n])
            while k and c:
                ans.append(list(n))
                c-=1
                k-=1
        return ans