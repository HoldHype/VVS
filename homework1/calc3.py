import math as m

class calculator():
    def __init__(self, num1: int, num2: int, znak: str):
        self.num1 = num1
        self.num2 = num2
        self.znak = znak


    def calc(num1: int, num2: int, znak: str) -> int: 
        if znak == '+':
            return(num1 + num2)
        elif znak == '-':
            return(num1 - num2)
        elif znak == '*':
            return(num1 * num2)
        elif znak == '/':
            return(num1 / num2)
        
    def ing_calc(operation: 'str', num: int) -> float:
        if operation == 'cos':
            return m.cos(num)
        elif operation == 'sin':
            return m.sin(num)

print('Выберете калькулятор: 1.обычный 2.инженерный: ')
choice = int(input())
if choice == 1:
    number1 = int(input('Введите первое число: '))
    number2 = int(input('Введите второе число: '))
    znak = input('Введите знак операции: ')
    print(calculator.calc(number1, number2, znak))
elif choice == 2:
    number = int(input('Введите число: '))
    operation = input('Выберете функцию: ')
    print(calculator.ing_calc(operation, number))