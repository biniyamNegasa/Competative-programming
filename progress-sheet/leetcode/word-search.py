class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])
        sz = len(word)

        inbound = lambda r,c: -1<r<n and -1<c<m
        DIR = [[0,-1],[0,1],[-1,0],[1,0]]

        def trav(r, c, ind):
            if ind==sz:
                return True
            if not inbound(r,c) or board[r][c]!=word[ind]:
                return False
            
            board[r][c] = '?'
            for i,j in DIR:
                if trav(r+i, c+j, ind+1):
                    return True
            board[r][c] = word[ind]
            return False
        for i in range(n):
            for j in range(m):
                if board[i][j]==word[0] and trav(i,j,0):
                    return True
        return False