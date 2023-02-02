class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        maxRow, maxCol = len(board), len(board[0])
        path = set()
        
        def bfs(row, col, i):
            if(i == len(word)):
                return True
            if(min(row, col) < 0 or row >= maxRow or col >= maxCol or word[i] != board[row][col] or (row, col) in path):
                return False

            path.add((row, col))
            directions = [1, 0, -1, 0, 1]
            res = (
                bfs(row + 1, col, i + 1)
                or bfs(row - 1, col, i + 1)
                or bfs(row, col + 1, i + 1)
                or bfs(row, col - 1, i + 1)
            )
            path.remove((row, col))
            return res
            
        count = defaultdict(int, sum(map(Counter, board), Counter()))
        if count[word[0]] > count[word[-1]]:
            word = word[::-1]

        for row in range(maxRow):
            for col in range(maxCol):
                if(bfs(row, col, 0)):
                    return True
        return False