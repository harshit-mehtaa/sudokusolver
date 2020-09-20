class SudokuSolver:
    _sudoku = [
        [3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]
    ]

    @property
    def sudoku(self):
        return self._sudoku

    @sudoku.setter
    def sudoku(self, sudoku):
        self._sudoku = sudoku

    def __init__(self, arr=None):
        if arr:
            self.sudoku = arr

    def print_grid(self):
        for i in range(9):
            print()
            if i % 3 == 0 and i != 0:
                print('- ' * 13)

            for j in range(9):
                if j % 3 == 2 and j != 8:
                    print(self.sudoku[i][j], end='| ')
                else:
                    print(self.sudoku[i][j], end='  ')
        return None

    def find_empty_cell(self):
        for row in range(9):
            for col in range(9):
                if self.sudoku[row][col] == 0:
                    return row, col
        return None

    def exists_in_row(self, row, number):
        return number in self.sudoku[row]

    def exists_in_col(self, col, number):
        return number in [row[col] for row in self.sudoku]

    def exists_in_mini_grid(self, row, col, number):
        box_x = col // 3
        box_y = row // 3

        for i in range(box_y * 3, box_y * 3 + 3):
            for j in range(box_x * 3, box_x * 3 + 3):
                if self.sudoku[i][j] == number and (i, j) != (row, col):
                    return True
        return False

    def cell_is_safe(self, row, col, number):
        return not self.exists_in_row(row, number) and not self.exists_in_col(col, number) and not self.exists_in_mini_grid(row, col, number)

    def solve(self):
        cell = self.find_empty_cell()

        if not cell:
            return True
        row, col = cell

        for number in range(1, 10):
            if self.cell_is_safe(row, col, number):
                self.sudoku[row][col] = number

                if self.solve():
                    return True
                self.sudoku[row][col] = 0
        return False


if __name__ == '__main__':
    solver = SudokuSolver()

    solver.solve()
    solver.print_grid()
