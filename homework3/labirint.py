import random


def move(matrix: list, pos: list, x: int, y: int) -> int:
    if matrix[x][y] not in 'П!$_#':
        matrix[x][y] = '*'
    step = str(input('Выбери куда хочешь пойти: '))
    if step == 'w': x -= 1
    elif step == 's': x += 1
    elif step == 'd': y += 1
    elif step == 'a': y -= 1
    elif step == 'end': 
        print('Возврашайся(((')
        exit()
    else: print('Такой команды нет')
    if matrix[x][y] not in 'П!$_#':
        matrix[x][y] = 'I'
    return x, y


def check(x: int, y: int) -> int:
    if x < 0: x = 0
    elif x > 9: x = 9
    elif y < 0: y = 0
    elif y > 9: y = 9
    return x, y

def random_pos(matrix: list, pos: list):
    pos_key = random.choice(pos)
    matrix[pos_key[0]][pos_key[1]] = '$'
    pos.remove(pos_key)
    pos_roshan = random.choice(pos)
    matrix[pos_roshan[0]][pos_roshan[1]] = '!'
    pos.remove(pos_roshan)
    pos_portal = random.choice(pos)
    matrix[pos_portal[0]][pos_portal[1]] = 'П'
    pos.remove(pos_portal)
    pos_trap = random.choice(pos)
    matrix[pos_trap[0]][pos_trap[1]] = '_'
    pos.remove(pos_trap)
    pos_chest = random.choice(pos)
    matrix[pos_chest[0]][pos_chest[1]] = '#'
    pos.remove(pos_chest)
    return matrix

def actions(matrix: list, x: int, y: int, key: int, hp: int, weapon: int):
    if matrix[x][y] == '$':
        print('Поздравляю!! ты нашел ключ, теперь ты можешь выйти через портал')
        key+=1
    if matrix[x][y] == 'П':
        if key == 0:
            print('Ты нашел портал, но у тебя нет ключа, ты не можешь выйти')
        elif key > 0:
            print('Поздравляю, ты можешь выйти из лабиринта')
            exit()
    if matrix[x][y] == '_':
        print('Ты наступил на ловушку')
        hp -= 1
    if matrix[x][y] == '!':
        if weapon == 0:
            print('Ты попал в логово рошана, но у тебя нет оружия, ты отхватил от него по полной')
            hp-=1
        else:
            print('В ожесточенной борьбе ты убил рошана и получил аегис, но твое оружие сломалось')
            hp+=1
            weapon-=1
    if matrix[x][y] == '#':
        print('Ты нашел сундук, хочешь его открыть?')
        d = input()
        if d == 'yes':
            r = random.randint(1,3)
            if r == 1:  
                print('ты нашел зелье здоровья')
                hp+=1
            if r == 2: 
                print('ты нашел рапиру')
                weapon+=1
            if r == 3: 
                print('ты нашел ключ')
                key+=1
        elif d == 'no':
            print('тебе виднее')
    return key, hp, weapon

    






matrix = [['*' for x in range(10)] for x in range(10)]
pos = [[x, y] for x in range(10) for y in range(10)]
matrix = random_pos(matrix, pos)
hp = 3
x = 0
y = 0
key = 0
weapon = 0
matrix[x][y] = 'I'
print('Добро пожаловать в игру, вот основное управление и обозначение: a - влево s - вниз d - вправо w - вверх П - портал # - сундук ! - рошан $ - ключ')
print(*matrix, sep = '\n')
while hp > 0:
    x, y = move(matrix, pos, x, y)
    x, y = check(x, y)
    key, hp, weapon = actions(matrix, x, y, key, hp, weapon)
    print('Твои координаты: ', y + 1, x + 1)
    print('Твое здоровье: ', hp)
    print('Ключи: ', key)
    print(*matrix, sep = '\n')
print('Смерть в нищете(')
