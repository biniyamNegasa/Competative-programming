class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        mx1 = 0
        L = 0
        c=k
        for R in range(len(answerKey)):
            if answerKey[R]=='F' and not c:
                while answerKey[L]=='T':
                    L+=1
                if answerKey[L]=='F':
                    c+=1
                L+=1
            if answerKey[R]=='F':
                c-=1
            mx1 = max(mx1, R-L+1)
        mx2 = 0
        L = 0
        for R in range(len(answerKey)):
            if answerKey[R]=='T' and not k:
                while answerKey[L]=='F':
                    L+=1
                if answerKey[L]=='T':
                    k+=1
                L+=1
            if answerKey[R]=='T':
                k-=1
            mx2 = max(mx2, R-L+1)
        return max(mx1, mx2)