class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        q = collections.deque()

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    q.append((i, j))
        if not q or len(q) == n * n: return -1

        ans = -1
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while q:
            size = len(q)
            ans += 1
            while(size):
                size -=1
                row, col = q.popleft()
                directions = [0, 1, 0,-1, 0]
                for dx, dy in dirs:
                    newRow = row + dx
                    newCol = col + dy
                    if(0 <= newRow < n and 0 <= newCol < n and grid[newRow][newCol] == 0):
                        grid[newRow][newCol] = 1
                        q.append((newRow, newCol))

        return ans