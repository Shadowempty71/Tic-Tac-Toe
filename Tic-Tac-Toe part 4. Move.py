field =[['-'] * 3 for i in range(3)] # игровое поле
field[2][2] = 'X'

def move():
    while True:
        x_y = input("Ваш ход. Введите числа через пробел:").split()
        if len(x_y) != 2 :
            print("Вы ввели не верные координаты. Попробуйте ввести числа через пробел")
            continue
        else:
            x,y = x_y
        if not(x.isdigit()) or not(y.isdigit()):
            print("Одна или обе координаты не являются цифрами. Вводите координаты правильно")
            continue
        else:
            x,y = int(x),int(y)
        if any((2 < item) or (item < 0) for item in(x, y)):
            print("Ход недопустим, - выбранная клетка вне игрового поля.Попробуйте сходить иначе")
            continue
        elif field[x][y] != '-':
            print("Ход недопустим, - выбранная клетка занята.Попробуйте сходить иначе")
            continue
        else:
            return x,y
print(move())