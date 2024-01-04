class Solution:
    def smallestNumber(self, num: int) -> int:
        if num<0:
            n = [*str(num)[1:]]
            n.sort(reverse=True)
            return -1*int(''.join(n))
        n = [*str(num)]
        n.sort()
        L = 0
        R = 1
        while n[L]=='0' and R<len(n):
            if n[R]!='0':
                n[L], n[R] = n[R], n[L]
            R+=1
        return int(''.join(n))