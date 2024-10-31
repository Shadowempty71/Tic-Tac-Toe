field =[['-'] * 3 for i in range(3)] # игровое поле
field[0][2] = 'X'
field[0][0] = 'X'
field[0][1] = 'X'


def demonstration():# функция вывода игрового поля в консоль в консоль
    print(f"  0 1 2")
    print(f"0 {field[0][0]} {field[0][1]} {field[0][2]}")
    print(f"1 {field[1][0]} {field[1][1]} {field[1][2]}")
    print(f"2 {field[2][0]} {field[2][1]} {field[2][2]}")
demonstration()
def win_comb():
    comb = [((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
            ((0, 0), (1, 1), (2, 2)), ((2, 0), (1, 1), (0, 2)), ((0, 0), (1, 0), (2, 0)),
            ((0, 2), (1, 2), (2, 2)), ((0, 1), (1, 1), (2, 1))]
    for c in comb:
        a, b, c, d, e, f, g, h = comb[0], comb[1], comb[2], comb[3], comb[4], comb[5], comb[6], comb[7]

    if field in comb:
        print(f"Выиграл{field[c][c]}")
win_comb()