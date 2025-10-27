def lvl1() -> str:    
    text = str(input('Введите сторку: '))
    # text_1 = str('прИвЕт МИР')
    func = int(input('Выберете функцию: 1. upper 2. lower 3.capitalize'))
    if func == 1:
        print(text.upper())
    if func == 2:
        print(text.lower())
    if func == 3:
        print(text.capitalize())

def lvl2():
    text = str('Ботать - это круто. Очень круто!')
    func = int(input('Выберете функцию: 1. find 2. replace 3.count \n'))
    if func == 1:
        word = str(input('Выберете слово для поиска: '))
        print(text.find('круто'))
    if func == 2:
        word = str(input('Выберете слово для замены: '))
        print(text.replace('круто', word))
    if func == 3:
        word = str(input('Выберете букву для поиска: '))
        print(text.count('о'))

def lvl3() -> str:
    text = '1,2,3,4,5'
    func = int(input('Выберете функцию: 1. split 2. join \n'))
    if func == 1:
        print(text.split(','))
    elif func == 2:
        word = str(input('Выберете знак для склейки: '))
        print(word.join(text.split(',')))

def lvl4():
    text = ['lop', 'lop**', '1234', '123p']
    text_index = int(input('Выберете текст: '))
    func = int(input('Выберете функцию: 1. isdigit 2. isalpha 3. strip \n'))
    if func == 1:
        print(text[text_index - 1].isdigit())
    if func == 2:
        print(text[text_index - 1].isalpha())
    if func == 3:
        print(text[text_index - 1].strip())

def lvl5():
    text = '   pYthon;is;Awesome;   '
    print(' '.join(text.strip().split(';')).capitalize())

    
choice = int(input('Выберете уровень: '))
if choice == 1: lvl1()
if choice == 2: lvl2()
if choice == 3: lvl3()
if choice == 4: lvl4()
if choice == 5: lvl5()
else: print('Такого уровня еще нет(((')

