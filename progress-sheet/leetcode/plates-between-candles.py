class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        ps = []
        candle = []
        for i,ch in enumerate(s):
            if ch=='*':
                if ps:
                    ps.append(ps[-1]+1)
                else:
                    ps.append(1)
            else:
                candle.append(i)
                if ps:
                    ps.append(ps[-1])
                else:
                    ps.append(0)
        for s,e in queries:
            l = bisect_left(candle, s)
            r = bisect_right(candle,e)-1
            if l>r:
                yield 0
            else:
                yield (ps[candle[r]]-ps[candle[l]])