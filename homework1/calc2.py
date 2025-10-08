def sum_num(num1: int, num2: int) -> int: 
    return int(num1 + num2)

def sub_num(num1: int, num2: int) -> int: 
    return int(num1 - num2)

def mult_num(num1: int, num2: int) -> int: 
    return int(num1 * num2)

def del_num(num1: int, num2: int) -> int: 
    return int(num1 / num2)

number1 = int(input('Введите первое число: '))
number2 = int(input('Введите второе число: '))
znak = input('Введите знак операции: ')
if znak == '+':
    print(sum_num(number1, number2))
elif znak == '-':
    print(sub_num(number1, number2))
elif znak == '*':
    print(mult_num(number1,number2))
elif znak == '/':
    print(del_num(number1, number2))