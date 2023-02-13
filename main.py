def output(table):
    """Данная функция производит вывод игрового поля на  экран"""

    print()
    print('   ', *['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', ''], sep=' \ ')
    print('   ----------------------------------')
    for n, i in enumerate(table):
        print(f'({n + 1})', *i, f'({n + 1})', sep=' | ')
        if n == 7:
            break
        print('   ----------------------------------')
    print('   ----------------------------------')
    print('   ', *['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', ''], sep=' / ')
    print()


def no_way(problem=''):
    """Данная функция предназначена для вызова во время игры при ошибочном и/или направильном вводе хода игроком."""

    print(problem)
    global user_step
    user_step = input('Попробуй еще раз! Введите ваш ход в формате A1-B4. Игрок {} >'.format(player))
    if table[int(user_step[1]) - 1][step_dict[user_step[0]]] == 'p' or table[int(user_step[1]) - 1][step_dict[user_step[0]]] == 'P':
        pawn(user_step)
    elif table[int(user_step[1]) - 1][step_dict[user_step[0]]] == 'n' or table[int(user_step[1]) - 1][step_dict[user_step[0]]] == 'N':
        horse(user_step)
    elif table[int(user_step[1]) - 1][step_dict[user_step[0]]] == 'k' or table[int(user_step[1]) - 1][step_dict[user_step[0]]] == 'K':
        queen(user_step)
    elif table[int(user_step[1]) - 1][step_dict[user_step[0]]] == 'r' or table[int(user_step[1]) - 1][step_dict[user_step[0]]] == 'R':
        rook(user_step)
    elif table[int(user_step[1]) - 1][step_dict[user_step[0]]] == 'b' or table[int(user_step[1]) - 1][step_dict[user_step[0]]] == 'B':
        bishop(user_step)
    elif table[int(user_step[1]) - 1][step_dict[user_step[0]]] == 'k' or table[int(user_step[1]) - 1][step_dict[user_step[0]]] == 'K':
        king(user_step)


def pawn(user_step_inf):
    """ Данная функция проверяет ход пешки на ход из начальной позиции, на ход из другой позиции,
    проверяет ход пешки при взятии другой фигуры согласно правилам шахмат.

    """
    global player

    if table[int(user_step_inf[1]) - 1][step_dict[user_step_inf[0]]] in player_shapes: # Проверка на фигуру игрока
        if (abs(step_dict[user_step_inf[0]] - step_dict[user_step_inf[3]]) == 1 # Проверка на шаг - взятие, при которой съедаемая фигура не король
                and abs(int(user_step_inf[4]) - int(user_step_inf[1])) == 1
                and table[int(user_step_inf[4]) - 1][step_dict[user_step_inf[3]]] != ' '
                and table[int(user_step_inf[4]) - 1][step_dict[user_step_inf[3]]] != 'Q'
                and table[int(user_step_inf[4]) - 1][step_dict[user_step_inf[3]]] not in player_shapes):

            table[int(user_step_inf[4]) - 1][step_dict[user_step_inf[3]]] = table[int(user_step_inf[1]) - 1][step_dict[user_step_inf[0]]]
            table[int(user_step_inf[1]) - 1][step_dict[user_step_inf[0]]] = ' '

            player = 1 if player == 2 else 2

        else:
            if int(user_step_inf[1]) == 2 or int(user_step_inf[1]) == 7:  # Ход из начальной позиции
                if (table[int(user_step_inf[4]) - 1][step_dict[user_step_inf[3]]] != ' '  # проверка на шаг в перед и длину не более 2х
                        or abs(int(user_step_inf[4]) - int(user_step_inf[1])) > 2
                        or user_step_inf[0] != user_step_inf[3]):
                    no_way()

                else:
                    table[int(user_step_inf[4]) - 1][step_dict[user_step_inf[3]]] = table[int(user_step_inf[1]) - 1][step_dict[user_step_inf[0]]]
                    table[int(user_step_inf[1]) - 1][step_dict[user_step_inf[0]]] = ' '

                    player = 1 if player == 2 else 2
            else:
                if (table[int(user_step_inf[4]) - 1][step_dict[user_step_inf[3]]] != ' ' # проверка на шаг вперед и длину не более 1
                        or (abs(int(user_step_inf[4]) - int(user_step_inf[1])) > 1
                            or user_step_inf[0] != user_step_inf[3])):
                    no_way()

                else:
                    table[int(user_step_inf[4]) - 1][step_dict[user_step_inf[3]]] = table[int(user_step_inf[1]) - 1][step_dict[user_step_inf[0]]]
                    table[int(user_step_inf[1]) - 1][step_dict[user_step_inf[0]]] = ' '

                    player = 1 if player == 2 else 2

    else:
        no_way('Ты используешь не свои фигуры!')


def horse(user_step_inf):
    """ Данная функция предназначена для проверки хода Конем, проверки возможности взятия фигурой фигуру оппонента"""
    global player

    if table[int(user_step_inf[1]) - 1][step_dict[user_step_inf[0]]] in player_shapes:  # Проверка на фигуру игрока
        if ((abs(step_dict[user_step_inf[0]] - step_dict[user_step_inf[3]]) == 1    # Проверка на шаг буквой "Г" и проверка на съедаемую фигуру
             and abs(int(user_step_inf[4]) - int(user_step_inf[1])) == 2
             and table[int(user_step_inf[4]) - 1][step_dict[user_step_inf[3]]] not in player_shapes)
                or (abs(step_dict[user_step_inf[0]] - step_dict[user_step_inf[3]]) == 2
                    and abs(int(user_step_inf[4]) - int(user_step_inf[1])) == 1
                    and table[int(user_step_inf[4]) - 1][step_dict[user_step_inf[3]]] not in player_shapes)):

            table[int(user_step_inf[4]) - 1][step_dict[user_step_inf[3]]] = table[int(user_step_inf[1]) - 1][step_dict[user_step_inf[0]]]
            table[int(user_step_inf[1]) - 1][step_dict[user_step_inf[0]]] = ' '

            player = 1 if player == 2 else 2

        else:
            no_way('Не правильный ход фигурой!')

    else:
        no_way('Ты используешь не свои фигуры!')


def rook(user_step_inf):
    """ Данная функция предназначена для проверки хода Ладьей, проверки возможности взятия фигурой фигуру оппонента"""
    global player

    if table[int(user_step_inf[1]) - 1][step_dict[user_step_inf[0]]] in player_shapes:  # Проверка на фигуру игрока, проверка на шаг по вертикали или горизонтали
        if (step_dict[user_step_inf[0]] == step_dict[user_step_inf[3]]
                and table[int(user_step_inf[4]) - 1][step_dict[user_step_inf[3]]] not in player_shapes):

            step = 1 if (int(user_step_inf[1]) <= int(user_step_inf[4])) else -1

            for r in range(int(user_step_inf[1]) + step, int(user_step_inf[4]), step):
                if table[int(user_step_inf[r-step]) ][step_dict[user_step_inf[0]]] != ' ':  # Если на пути по вертикали есть фигура
                    print('Не правильный ход фигурой!')
                    return False

            table[int(user_step_inf[4]) - 1][step_dict[user_step_inf[3]]] = table[int(user_step_inf[1]) - 1][step_dict[user_step_inf[0]]]
            table[int(user_step_inf[1]) - 1][step_dict[user_step_inf[0]]] = ' '

            player = 1 if player == 2 else 2

        elif (int(user_step_inf[1]) == int(user_step_inf[4])
              and table[int(user_step_inf[4]) - 1][step_dict[user_step_inf[3]]] not in player_shapes):

            step = 1 if (step_dict[user_step_inf[0]] <= step_dict[user_step_inf[3]]) else -1

            for r in range(step_dict[user_step_inf[0]] + step , step_dict[user_step_inf[3]], step):
                if table[int(user_step_inf[1])-1][r] != ' ':    # Если на пути по горизонтали есть фигура
                    print('Не правильный ход фигурой!')
                    return False

            table[int(user_step_inf[4]) - 1][step_dict[user_step_inf[3]]] = table[int(user_step_inf[1]) - 1][step_dict[user_step_inf[0]]]
            table[int(user_step_inf[1]) - 1][step_dict[user_step_inf[0]]] = ' '

            player = 1 if player == 2 else 2

        else:
            no_way('Не правильный ход фигурой!')

    else:
        no_way('Используешь не свои фигуры!')


def queen(user_step_inf):
    """ Данная функция предназначена для проверки хода Ферзем, проверки возможности взятия фигурой фигуру оппонента"""
    global player

    if table[int(user_step_inf[1]) - 1][step_dict[user_step_inf[0]]] in player_shapes:  # Проверка на фигуру игрока
        if (step_dict[user_step_inf[0]] == step_dict[user_step_inf[3]]
                and table[int(user_step_inf[4]) - 1][step_dict[user_step_inf[3]]] not in player_shapes): # проверка на шаг по вертикали и проверка на фигуру игрока

            step = 1 if (int(user_step_inf[1]) <= int(user_step_inf[4])) else -1

            for r in range(int(user_step_inf[1]) + step, int(user_step_inf[4]), step):
                if table[int(user_step_inf[r-step]) ][step_dict[user_step_inf[0]]] != ' ':  # Если на пути по вертикали есть фигура
                    print('Не правильный ход фигурой!')
                    return False

            table[int(user_step_inf[4]) - 1][step_dict[user_step_inf[3]]] = table[int(user_step_inf[1]) - 1][step_dict[user_step_inf[0]]]
            table[int(user_step_inf[1]) - 1][step_dict[user_step_inf[0]]] = ' '

            player = 1 if player == 2 else 2

        elif (int(user_step_inf[1]) == int(user_step_inf[4])
              and table[int(user_step_inf[4]) - 1][step_dict[user_step_inf[3]]] not in player_shapes): # проверка на шаг по горизонтали и проверка на фигуру игрока

            step = 1 if (step_dict[user_step_inf[0]] <= step_dict[user_step_inf[3]]) else -1

            for r in range(step_dict[user_step_inf[0]] + step , step_dict[user_step_inf[3]], step):
                if table[int(user_step_inf[1])-1][r] != ' ':    # Если на пути по горизонтали есть фигура
                    print('Не правильный ход фигурой!')
                    return False

            table[int(user_step_inf[4]) - 1][step_dict[user_step_inf[3]]] = table[int(user_step_inf[1]) - 1][step_dict[user_step_inf[0]]]
            table[int(user_step_inf[1]) - 1][step_dict[user_step_inf[0]]] = ' '

            player = 1 if player == 2 else 2

        elif (abs(step_dict[user_step_inf[0]] - step_dict[user_step_inf[3]]) == abs(int(user_step_inf[1]) - int(user_step_inf[4]))
              and table[int(user_step_inf[4]) - 1][step_dict[user_step_inf[3]]] not in player_shapes):  # проверка на шаг по диагонали и проверка на фигуру игрока

            step = 1 if (int(user_step_inf[1]) <= int(user_step_inf[4])) else -1
            step_2 = 1 if (step_dict[user_step_inf[0]] <= step_dict[user_step_inf[3]]) else -1

            for i in range(1, abs(step_dict[user_step[0]] - step_dict[user_step[3]])):  # Есть ли на пути по диагонали фигура
                if table[int(user_step_inf[1]) - 1 + step_2 * i][step_dict[user_step_inf[0]] + step * i] != ' ':
                    print('Не правильный ход фигурой!')
                    return False

            table[int(user_step_inf[4]) - 1][step_dict[user_step_inf[3]]] = table[int(user_step_inf[1]) - 1][step_dict[user_step_inf[0]]]
            table[int(user_step_inf[1]) - 1][step_dict[user_step_inf[0]]] = ' '

            player = 1 if player == 2 else 2

        else:
            no_way('Не правильный ход фигурой!')
    else:
        no_way('Ты используешь не свои фигуры!')


def bishop(user_step_inf):
    """ Данная функция предназначена для проверки хода Слоном, проверки возможности взятия фигурой фигуру оппонента"""
    global player

    if table[int(user_step_inf[1]) - 1][step_dict[user_step_inf[0]]] in player_shapes:  # Проверка на фигуру игрока
        if (abs(step_dict[user_step_inf[0]] - step_dict[user_step_inf[3]]) == abs(int(user_step_inf[1]) - int(user_step_inf[4]))
                and table[int(user_step_inf[4]) - 1][step_dict[user_step_inf[3]]] not in player_shapes):    # проверка на шаг по диагонали и проверка на фигуру игрока

            step = 1 if (int(user_step_inf[1]) <= int(user_step_inf[4])) else -1
            step_2 = 1 if (step_dict[user_step_inf[0]] <= step_dict[user_step_inf[3]]) else -1

            for i in range(1, abs(step_dict[user_step[0]] - step_dict[user_step[3]])):
                if table[int(user_step_inf[1]) - 1 + step_2 * i][step_dict[user_step_inf[0]] + step * i] != ' ':    # Есть ли на пути по диагонали фигура
                    print('Не правильный ход фигурой!')
                    return False

            table[int(user_step_inf[4]) - 1][step_dict[user_step_inf[3]]] = table[int(user_step_inf[1]) - 1][step_dict[user_step_inf[0]]]
            table[int(user_step_inf[1]) - 1][step_dict[user_step_inf[0]]] = ' '

            player = 1 if player == 2 else 2

        else:
            no_way('Не правильный ход фигурой!')

    else:
        no_way('Ты используешь не свои фигуры!')


def king(user_step_inf):
    """ Данная функция предназначена для проверки хода Королем, проверки возможности взятия фигурой фигуру оппонента"""
    global player

    if table[int(user_step_inf[1]) - 1][step_dict[user_step_inf[0]]] in player_shapes:
        if (abs(step_dict[user_step_inf[0]] - step_dict[user_step_inf[3]]) == 1
                or abs(int(user_step_inf[4]) - int(user_step_inf[1])) == 1
                or abs(step_dict[user_step_inf[0]] - step_dict[user_step_inf[3]]) == abs(int(user_step_inf[1]) - int(user_step_inf[4])) == 1
                and table[int(user_step_inf[4]) - 1][step_dict[user_step_inf[3]]] not in player_shapes):

            table[int(user_step_inf[4]) - 1][step_dict[user_step_inf[3]]] = table[int(user_step_inf[1]) - 1][step_dict[user_step_inf[0]]]
            table[int(user_step_inf[1]) - 1][step_dict[user_step_inf[0]]] = ' '

            player = 1 if player == 2 else 2

        else:
            no_way("Не правильный ход фигурой!")

    else:
        no_way('Ты используешь не свои фигуры!')


table = [['r', 'n', 'b', 'q', 'k', 'b', 'm', 'r'],
         ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
         [' ', ' ', ' ', ' ', ' ', 'P', ' ', ' '],
         [' ', ' ', 'e', ' ', 'K', ' ', ' ', ' '],
         [' ', ' ', ' ', 'p', ' ', ' ', 'p', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
         ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']]

player = 2
player_shapes = ['r', 'n', 'b', 'q', 'k', 'b', 'm', 'r', 'p'] if player == 1 else ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R', 'P']
step_dict = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}


while True:
    output(table)
    user_step = input('Введите ваш ход в формате a1-b4. Игрок {}>'.format(player))

    # ПЕШКА
    if (table[int(user_step[1]) - 1][step_dict[user_step[0]]] == 'p'
            or table[int(user_step[1]) - 1][step_dict[user_step[0]]] == 'P'):
        pawn(user_step)

    # КОНЬ
    elif (table[int(user_step[1]) - 1][step_dict[user_step[0]]] == 'n'
          or table[int(user_step[1]) - 1][step_dict[user_step[0]]] == 'N'):
        horse(user_step)

    # Ферзь
    elif (table[int(user_step[1]) - 1][step_dict[user_step[0]]] == 'k'
          or table[int(user_step[1]) - 1][step_dict[user_step[0]]] == 'K'):
        queen(user_step)

    # Ладья
    elif (table[int(user_step[1]) - 1][step_dict[user_step[0]]] == 'r'
          or table[int(user_step[1]) - 1][step_dict[user_step[0]]] == 'R'):
        rook(user_step)

    # Слон
    elif (table[int(user_step[1]) - 1][step_dict[user_step[0]]] == 'b'
          or table[int(user_step[1]) - 1][step_dict[user_step[0]]] == 'B'):
        bishop(user_step)

    # Король
    elif (table[int(user_step[1]) - 1][step_dict[user_step[0]]] == 'k' or table[int(user_step[1]) - 1][step_dict[user_step[0]]] == 'K'):
        king(user_step)