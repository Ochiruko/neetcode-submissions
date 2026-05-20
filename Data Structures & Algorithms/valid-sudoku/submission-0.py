def getRows(board: List[List[str]]) -> List[str]:
    return board


def getCols(board: List[List[str]]) -> List[str]:
    return [[board[i][j] for i in range(9)] for j in range(9)]


def getSquares(board: List[List[str]]) -> List[str]:
    squares = []
    for triple_row in [0, 3, 6]:
        for triple_col in [0, 3, 6]:
            squares.append(
                [board[triple_row + i][triple_col + j] for i in range(3) for j in range(3)]
            )
    return squares

def repeated_number(entries: List[str]) -> bool:
    seen = [False for i in range(len(entries))]
    for entry in entries:
        if entry.isdigit():
            if seen[int(entry) - 1]:
                return True
            seen[int(entry) - 1] = True
    return False


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for entries in getRows(board) + getCols(board) + getSquares(board):
            if repeated_number(entries):
                print(entries)
                return False
        return True
