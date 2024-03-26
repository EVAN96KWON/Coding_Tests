class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            if not self.is_valid(row):
                return False
        for col in zip(*board):
            if not self.is_valid(col):
                return False
        cells = [row[3 * i : 3 * (i + 1)] for i in range(3) for row in board]
        for i in range(0, len(cells), 3):
            cell = [i for row in cells[i : i + 3] for i in row]
            if not self.is_valid(cell):
                return False
        return True

    def is_valid(self, line: List[str]) -> bool:
        line = list(filter(lambda x: x != ".", line))
        return len(set(line)) == len(line)
