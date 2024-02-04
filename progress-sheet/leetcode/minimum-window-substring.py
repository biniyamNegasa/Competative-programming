class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        t_c = Counter(t)
        dic = defaultdict(int)
        f_ind = -1
        l_ind = -1
        ans = n+1
        L = 0
        tot = len(t)
        curr = 0
        for R in range(len(s)):
            dic[s[R]]+=1
            if  s[R] in t_c and dic[s[R]]<=t_c[s[R]]:
                curr+=1
            while curr==tot:
                if R-L+1<ans:
                    ans = R-L+1
                    f_ind = L
                    l_ind = R
                dic[s[L]]-=1
                if dic[s[L]]<t_c[s[L]]:
                    curr-=1
                L+=1
        return s[f_ind:l_ind+1] if f_ind!=-1 else '' 