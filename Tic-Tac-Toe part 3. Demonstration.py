field =[['-'] * 3 for i in range(3)] # игровое поле
field[0][2] = 'X'


def demonstration():# функция вывода игрового поля в консоль в консоль
    print(f"  0 1 2")
    print(f"0 {field[0][0]} {field[0][1]} {field[0][2]}")
    print(f"1 {field[1][0]} {field[1][1]} {field[1][2]}")
    print(f"2 {field[2][0]} {field[2][1]} {field[2][2]}")
demonstration()
