def greet():
    print("-------------------")
    print("  Приветсвуем вас  ")
    print("      в игре       ")
    print("  крестики-нолики  ")
    print("-------------------")
    print(" формат ввода: x y ")
    print(" x - номер строки  ")
    print(" y - номер столбца ")


def show():
    print(f'  | 0 | 1 | 2 |')
    print("---------------")
    for x, y in enumerate(field):
        stroka = " | ".join(y)
        print(f'{x} | {stroka} |')
        print("---------------")


def vvod():
    while True:

        dlina = input("Введите координаты ").split()

        if len(dlina) != 2:
            print("Введите две координаты")
            continue
        x, y = dlina
        if not x.isdigit() or not y.isdigit():
            print(" Введите числа! ")
            continue
        x, y = int(x), int(y)
        if 0 > x or x > 2 or 0 > y or y > 2:
            print("Введите корректные координаты")
            continue
        if field[x][y] != " ":
            print("Клетка занята")
            continue
        return x, y


def check_win():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for n in cord:
            symbols.append(field[n[0]][n[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграл Х")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл 0")
            return True
    return False


field = [[" "] * 3 for i in range(3)]
greet()
count = 0

while True:
    show()
    count += 1
    if count % 2 == 1:
        print("Ходит крестик")
    else:
        print("Ходит нолик")
    x, y = vvod()
    if count % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"
    if check_win():
        break

    if count == 9:
        print("Ничья")
        break

input('Press ENTER to exit')








