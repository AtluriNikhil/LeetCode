# Solution 1
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row_set = set()
            col_set = set()
            for j in range(9):
                if board[i][j] in row_set:
                    return False
                else:
                    if board[i][j] != ".":
                        row_set.add(board[i][j])
                if board[j][i] in col_set:
                    return False
                else:
                    if board[j][i] != ".":
                        col_set.add(board[j][i])
                if i%3 == 0 and j%3 == 0:
                    box_set = set()
                    for box_i in range(i, i+3):
                        for box_j in range(j, j+3):
                            if board[box_i][box_j] in box_set:
                                return False
                            else:
                                if board[box_i][box_j] != ".":
                                    box_set.add(board[box_i][box_j])
        return True

# Solution 2
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        res = []
        for i in range(9):
            for j in range(9):
                element = board[i][j]
                if element != '.':
                    res += [(i, element), (element, j), (i // 3, j // 3, element)]
        return len(res) == len(set(res))
