class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        # visited = set()
        # ((row, col) in visited)
        # visited.add((row, col))
        # (row, col) not in visited

        def dfs(row, col):
            if (row not in range(maxRow)) or (col not in range(maxCol)) or grid[row][col] == "0" or (row < 0) or (col < 0) or visited[row][col] == True:
                return 
            visited[row][col] = True
            
            directions = [1, 0, -1, 0, 1]

            for i in range(len(directions) -1):
                dfs(row + directions[i], col + directions[i + 1])

        maxRow = len(grid)
        maxCol = len(grid[0])
        islands = 0

        for row in range(maxRow):
            for col in range(maxCol):
                if(grid[row][col] == "1" and visited[row][col] == False):
                    islands += 1
                    dfs(row, col)
                    
        return islands