class Solution:
   
    def getTotalIsles(self, grid: list[list[str]]) -> int:
    #    write your code here

        def dfs(i,j):
            if 0 <=i < len(grid) and 0<=j < len(grid[0]) and grid[i][j] == 'L':
                grid[i][j] = 'V' 

                dfs(i+1,j)
                dfs(i-1,j)
                dfs(i,j+1)
                dfs(i,j-1)

        num_islands=0
        for i in range(len(grid)):
            for j in range ( len(grid[0])):
                if grid[i][j] == 'L' : 
                    num_islands += 1
                dfs (i,j)

        return num_islands               
        return 0

