class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        lst = {'2':['a','b','c'], '3':['d','e','f'], '4':['g','h','i'], '5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}
        ans = []
        n = len(digits)
        curr = []
        for ch in digits:
            curr.append(lst[ch])
        def com(i, arr):
            if i==n:
                if i:
                    ans.append(''.join(arr))
                return
            m = len(curr[i])
            for j in range(m):
                arr.append(curr[i][j])
                com(i+1, arr)
                arr.pop()
        com(0, [])
        return ans