class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        dic = defaultdict(int)
        mx = persons[0]
        self.times = times
        self.ans = []
        for person in persons:
            dic[person]+=1
            if dic[person]>=dic[mx]:
                mx = person
            self.ans.append(mx)

    def q(self, t: int) -> int:
        return self.ans[bisect_right(self.times,t)-1]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)