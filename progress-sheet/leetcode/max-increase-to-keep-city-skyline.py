class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        row = [max(a) for a in grid]
        clmn = []
        for j in range(len(grid[0])):
            mx = 0
            for i in range(len(grid)):
                mx = max(mx, grid[i][j])
            clmn.append(mx)
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                val = min(row[i], clmn[j])
                ans += val-grid[i][j] if val>grid[i][j] else 0
        return ans