def populate(s, max_col):
    matrix = [['?'] * max_col]
    col_increase = True
    row = col = 0
    for c in s:
        if not col_increase:
            matrix.append(['?'] * max_col)

        matrix[row][col] = c

        if col_increase:
            if col < max_col - 1:
                col += 1
            else:
                col_increase = False
                col -= 1
                row += 1
        else:
            if col > 0:
                col -= 1
                row += 1
            else:
                col_increase = True
                col += 1
    return matrix


def zigzag_print(m):
    for row in range(len(m[0])):
        line = []
        for col in range(len(m)):
            line.append(m[col][row])
        print line


s = 'PAYPALISHIRING'
m = populate(s, 3)
for x in m:
    print x
zigzag_print(m)
