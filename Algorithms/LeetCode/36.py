from typing import List

def isValidSudoku(board: List[List[str]]):
    ht = {}
    for i in range(9):
        ht[i] = [0] * 27

    for i in range(9):
        for j in range(9):
            if board[i][j] == ".":
                continue
            if ht[i][int(board[i][j]) - 1] == 0:
                ht[i][int(board[i][j]) - 1] = 1
            else:
                return False
            if ht[j][int(board[i][j]) + 9 - 1] == 0:
                ht[j][int(board[i][j]) + 9 - 1] = 1
            else:
                return False

            square_i = (i // 3 * 3 + j // 3)
            if ht[square_i][int(board[i][j]) + 9 * 2 - 1] == 0:
                ht[square_i][int(board[i][j]) + 9 * 2 - 1] = 1
            else:
                return False

    return True
