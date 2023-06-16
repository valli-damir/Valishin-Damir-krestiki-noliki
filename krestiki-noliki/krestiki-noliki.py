def Hello():
    print("Игра крестики-нолики")
    print("x - строка, "
          "y - столбец")

def playing_field():
    print(f"  | 0 | 1 | 2 |")
    print("---------------")
    for i in range(3):
        print(f"{i} {'|'} {field[i][0]} {'|'} {field[i][1]} {'|'} {field[i][2]} {'|'} ")
        print("---------------")

def place():
    while True:
        coordinat = input("Введите ваши координаты ").split()
        if len(coordinat) != 2:
            print("Введите 2 координаты ")
            continue
        x, y = coordinat
        if not(x.isdigit()) or not(y.isdigit()):
            print("Необхидимо ввести 2 числа ")
            continue
        x, y = int(x), int(y)
        if 0 <= x <= 2 and 0 <= y <= 2:
            if field[x][y] == " ":
                return x, y
            else:
                print("Клетка занята ")
        else:
            print("Координаты не удовлетваряют условиям ")

def win():
    win_cod = [((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
              ((0, 0), (1, 0), (2, 0)), ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)),
              ((0, 0), (1, 1), (2, 2)), ((2, 1), (1, 1), (0, 2)),]
    for i in range(3):
        simbol = []
        for j in range(3):
            simbol.append(field[i][j])
        if simbol == ["X", "X", "X"]:
            print("Выйграли крестики ")
            return True
        if simbol == ["0", "0", "0"]:
            print("Выйграли нолики ")
            return True
    for i in range(3):
        simbol = []
        for j in range(3):
            simbol.append(field[j][i])
        if simbol == ["X", "X", "X"]:
            print("Выйграли крестики ")
            return True
        if simbol == ["0", "0", "0"]:
            print("Выйграли нолики ")
            return True
    simbol = []
    for i in range(3):
        simbol.append(field[i][i])
    if simbol == ["X", "X", "X"]:
        print("Выйграли крестики ")
        return True
    if simbol == ["0", "0", "0"]:
        print("Выйграли нолики ")
        return True
    simbol = []
    for i in range(3):
        simbol.append(field[i][2-i])
    if simbol == ["X", "X", "X"]:
        print("Выйграли крестики ")
        return True
    if simbol == ["0", "0", "0"]:
        print("Выйграли нолики ")
        return True

    return False

Hello()
field = [[" ", " ", " "] for i in range(3)]
num = 0
while True:
    num += 1
    playing_field()
    if num % 2 == 1:
        print("Ходят крестики ")
    else:
        print("Ходят нолики ")
    x, y = place()
    if num % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"
    if win():
        break
    if num == 9:
        print("Ничья ")
        break
