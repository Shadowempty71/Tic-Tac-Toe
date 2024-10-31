# здесь будут выигрышные комбинации. 38
field =[['-'] * 3 for i in range(3)] # игровое поле
# field[0][2] = 'X'
# field[0][0] = 'X'
# field[0][1] = 'X'


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
    for a,b,c in comb:
        if field[a[0]][a[1]] == field[b[0]][b[1]] == field[c[0]][c[1]] != "-":
            return field[a[0][a[1]]