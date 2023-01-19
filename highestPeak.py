class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        maxRow, maxCol = len(isWater), len(isWater[0])
        height = [[-1] * maxCol for _ in range(maxRow)]

        q = collections.deque([])

        for row in range(maxRow):
            for col in range(maxCol):
                if(isWater[row][col] == 1):
                    q.append((row, col))
                    height[row][col] = 0

        directions = [0, 1, 0, -1, 0]

        while(q):
            row, col = q.popleft()
            for i in range(4):
                newRow, newCol = row + directions[i], col + directions[i + 1]
                if(newRow < 0 or newCol < 0 or newRow == maxRow or newCol == maxCol or height[newRow][newCol] != -1):
                    continue
                height[newRow][newCol] = height[row][col] + 1
                q.append((newRow, newCol))


        return height
