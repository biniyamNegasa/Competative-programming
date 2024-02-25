class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        q = deque()
        deck.sort(reverse=True)
        for d in deck:
            q.appendleft(d)
            q.appendleft(q.pop())
        q.append(q.popleft())
        return q