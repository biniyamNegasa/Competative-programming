class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        mat = [[0]*n for _ in range(m)]
        row = defaultdict(int)
        clmn = defaultdict(int)
        
        for i, j in guards:
            row[i]+=1
            clmn[j]+=1
        for i, j in walls:
            mat[i][j]=2
        
        for i, j in guards:
            mat[i][j]=1
            y = i
            x = j+1
            while x<n and y<m:
                if mat[y][x]==2:
                    break
                elif mat[y][x]==3:
                    break
                mat[y][x]=3
                x+=1
            y = i
            x = j-1
            while x>=0 and y<m:
                if mat[y][x]==2:
                    break
                elif mat[y][x]==3:
                    break
                mat[y][x]=3
                x-=1
            y = i+1
            x = j
            while x<n and y<m:
                if mat[y][x]==2:
                    break
                elif mat[y][x]==5:
                    break
                mat[y][x]=5
                y+=1
            y = i-1
            x = j
            while x<n and y>=0:
                if mat[y][x]==2:
                    break
                elif mat[y][x]==5:
                    break
                mat[y][x]=5
                y-=1
        count = 0
        for i in range(m):
            for j in range(n):
                if not mat[i][j]:
                    count+=1
        return count