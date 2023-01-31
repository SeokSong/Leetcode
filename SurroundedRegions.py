class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        maxRow, maxCol = len(board), len(board[0])
 
        def dfs(row, col):
            if(board[row][col] == "X"):
                return

            valid = True
            q = deque()
            q.append((row, col))
            visited = set()

            while(q):
                row, col = q.popleft()
                if row < 0 or col < 0 or col == maxCol or row == maxRow:
                    valid = False
                    break
                if board[row][col] == 'X' or (row, col) in visited:
                    continue
                
                directions = [1, 0, -1, 0, 1]
                visited.add((row, col))
                # q.append((row + 1, col))
                # q.append((row - 1, col))
                # q.append((row, col + 1))
                # q.append((row, col - 1))
                for i in range(len(directions) -1):
                    newRow = row + directions[i]
                    newCol = col + directions[i + 1]
                    q.append((newRow, newCol))

            if valid:
                for row, col in visited:
                    board[row][col] = 'X'

        for row in range(maxRow):
            for col in range(maxCol):
                dfs(row, col)
    