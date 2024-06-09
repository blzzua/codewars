# https://www.codewars.com/kata/65c796c193e1c20c1ae67209

def progress(puzzle: list[list[int]]) -> tuple[int,int,int]:
    for row in range(0, 9):
        for col in range(0, 9):
            if puzzle[row][col] == 0:
                digits = set()
                for i in range(9):
                    digits.add(puzzle[row][i]) # horizontal:
                    digits.add(puzzle[i][col]) # vertical
                row3 = (row//3) * 3
                col3 = (col//3) * 3
                # print(f'{col=}, {row=},{x0=}, {y0=}')
                for i in range(row3, row3 + 3):
                    for j in range(col3, col3 + 3):
                        if (0 <= i < 9) and (0 <= j < 9):
                            digits.add(puzzle[i][j]) # around
                if len(digits) == 9:
                    complement_digit = (set(range(10)) - set(digits)).pop()
                    return [row, col, complement_digit]
