class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen_rows = set()
        seen_cols = set()
        seen_squares = set()

        rows = len(board)
        cols = len(board[0])

        for row in range(rows):
            seen_rows.clear()
            for col in range(cols):
                if board[row][col] != ".":
                    if board[row][col] in seen_rows:
                        return False
                    else:
                        seen_rows.add(board[row][col])
        
        for col in range(cols):
            seen_cols.clear()
            for row in range(rows):
                if board[row][col] != ".":
                    if board[row][col] in seen_cols:
                        return False
                    else:
                        seen_cols.add(board[row][col])
        
        for square in range(9):
            seen_squares.clear()
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen_squares:
                        return False
                    seen_squares.add(board[row][col])
        return True
        


        


                
