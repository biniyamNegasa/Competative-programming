class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        dq = deque(senate)
        d_c = 0
        r_c = 0
        while len(dq)>1:
            val = dq.popleft()
            if val == 'D':
                if r_c>0:
                    r_c-=1
                else:
                    dq.append(val)
                    d_c+=1
            else:
                if d_c>0:
                    d_c-=1
                else:
                    dq.append(val)
                    r_c+=1
            if r_c>len(dq) or d_c>len(dq):
                return "Radiant" if dq[0]=='R' else "Dire"
        return "Radiant" if dq[0]=='R' else "Dire"