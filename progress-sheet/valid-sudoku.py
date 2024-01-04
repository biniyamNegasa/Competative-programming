class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                a = []
                if board[i][j]!='.':
                    a.append(int(board[i][j]))
                if board[i][j+1]!='.':
                    a.append(int(board[i][j+1]))
                if board[i][j+2]!='.':
                    a.append(int(board[i][j+2]))
                if board[i+1][j]!='.':
                    a.append(int(board[i+1][j]))
                if board[i+1][j+1]!='.':
                    a.append(int(board[i+1][j+1]))
                if board[i+1][j+2]!='.':
                    a.append(int(board[i+1][j+2]))
                if board[i+2][j]!='.':
                    a.append(int(board[i+2][j]))
                if board[i+2][j+1]!='.':
                    a.append(int(board[i+2][j+1]))
                if board[i+2][j+2]!='.':
                    a.append(int(board[i+2][j+2]))
                if len(set(a))!=len(a):
                    return False
        for i in range(9):
            a=[]
            for j in range(9):
                if board[i][j]!='.':
                    a.append(int(board[i][j]))
            if len(set(a))!=len(a):
                    return False
        for j in range(9):
            a=[]
            for i in range(9):
                if board[i][j]!='.':
                    a.append(int(board[i][j]))
            if len(set(a))!=len(a):
                    return False
        return True