class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #start in the middle and generate possible routes out to sea
        #we know  that [0, maxCol] and [maxRow, 0] are always solutions
        #maybe we use bfs for those 2 spots and check for height = or height + 1
        maxRow, maxCol = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(row, col, visited, height):
            if(row == maxRow or col == maxCol or col < 0 or row < 0 or (row, col) in visited or heights[row][col] < height):
                return
            # if(row < maxRow and
            # col < maxCol and
            # visited[row][col] != True and
            # row > 0 and col > 0 and
            # heights[row][col] >= height):
            # ans.append([row, col])
            visited.add((row, col))
            directions = [1, 0, -1, 0, 1]
            for i in range(len(directions) -1):
                newRow = row + directions[i]
                newCol = col + directions[i + 1]
                dfs(newRow, newCol, visited, heights[row][col])

        
        for col in range(maxCol):
            dfs(0, col, pac, heights[0][col])
            dfs(maxRow - 1, col, atl, heights[maxRow- 1][col])


        for row in range(maxRow):
            dfs(row, 0, pac, heights[row][0])
            dfs(row, maxCol - 1, atl, heights[row][maxCol - 1])

        ans = []

        for row in range(maxRow):
            for col in range(maxCol):
                if (row, col) in pac and (row, col) in atl:
                    ans.append([row, col])

        return ans