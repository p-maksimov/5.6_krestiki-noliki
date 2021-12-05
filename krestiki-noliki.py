# функция вывода игрового поля
def print_doska(desk):
    for row in desk:
        line = ''
        for cell in row:
            line += cell + " "
        print(line)

# проверка пользовательского ввода
def check_input(val):
    if val.isdecimal():
        val = int(val)
        if (1 > val) or (val > 3):
            print("Некорректный ввод! Введите число от 1 до 3.")
            return False
        else:
            return True
    else:
        print("Некорректный ввод! Введите число от 1 до 3.")
        return False


doska = [[' ', '1', '2', '3'],
         ['1', '-', '-', '-'],
         ['2', '-', '-', '-'],
         ['3', '-', '-', '-']]

PLAYER_X = "X"
PLAYER_0 = "0"
WIN_X = ["X", "X", "X"]
WIN_0 = ["0", "0", "0"]


player = PLAYER_X
game_over = False

# Игра начинается
while not game_over:
    # Печатаем доску
    print_doska(doska)
    # Блок ввода и проверки ввода
    if player == PLAYER_X:
        print("Ходит ИГРОК1 (КРЕСТИКИ)")
    else:
        print("Ходит ИГРОК2 (НОЛИКИ)")
    while True:
        x = input("Номер строки: ")
        if check_input(x):
            x = int(x)
            break
    while True:
        y = input("Номер столбца: ")
        if check_input(y):
            y = int(y)
            break

    stroka = doska[x]
    kletka = stroka[y]
    if kletka != "-":
        print("В эту клетку уже ходили! Повторите ход.")
        continue
    else:
        stroka[y] = player
        doska[x] = stroka

    # Блок определения победителя
    # 1 - проверка горизонталей
    for stroka in doska[1:3]:
        check = stroka[1:4]
        if check == WIN_X or check == WIN_0:
            game_over = True
            break

    # 2 - проверка вертикалей
    for i in range(1, 3):
        check = []
        for stroka in doska[1:3]:
            check.append(stroka[i])
        if check == WIN_X or check == WIN_0:
            game_over = True
            break

    # 3 - проверка диагоналей
    check = []
    check2 = []
    for i in range(1, 4):
        stroka = doska[i]
        check.append(stroka[i])
        check2.append(stroka[4-i])
    if check == WIN_X or check == WIN_0 or check2 == WIN_X or check2 == WIN_0:
        game_over = True
        break

    # Игра не окончена переход хода
    if not game_over:
        if player == PLAYER_X:
            player = PLAYER_0
        else:
            player = PLAYER_X

# конец основного цикла
print("\n"*2)
print_doska(doska)
if player == PLAYER_X:
    print("Игра окончена, победил ИГРОК1")
else:
    print("Игра окончена, победил ИГРОК2")
