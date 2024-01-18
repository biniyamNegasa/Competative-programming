class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        arr = [0]*(len(s)+1)
        for a, b, dr in shifts:
            if dr:
                arr[a]+=1
                arr[b+1]-=1
            else:
                arr[a]-=1
                arr[b+1]+=1
        ans = []
        curr = 0
        a_asc = ord('a')
        for i in range(len(s)):
            curr+=arr[i]
            if curr>=0:
                temp = (ord(s[i])+(curr%26))
                if temp>ord('z'):
                    temp-=26
                ans.append(chr(temp))
            else:
                temp = (ord(s[i])-((-curr)%26))
                if temp<a_asc:
                    temp+=26
                ans.append(chr(temp))
        return ''.join(ans)