class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        maxArea=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    area=self.dfs(grid, i, j)
                    maxArea= max(maxArea, area)
        return maxArea

    def dfs(self, grid, i, j):
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] == 0: 
            return 0

        grid[i][j] = 0
        
        return (1 +
                self.dfs(grid, i + 1, j) +
                self.dfs(grid, i - 1, j) +
                self.dfs(grid, i, j + 1) +
                self.dfs(grid, i, j - 1))

        