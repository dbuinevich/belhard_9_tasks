"""
Написать функцию check_phone, которая будет принимать строку и проверять,
что она соответствует шаблону:
1. код страны +375
2. код оператора 29, 33, 44, 25 в скобках
3. три цифры
4. тире
5. две цифры
6. тире
7 две цифры

Например: +375(29)365-12-12
"""
import re


def check_phone(number: str):
    pattern = r'^\+375\((29|33|44|25)\)\d{3}-\d{2}-\d{2}'
    if re.match(pattern, number):
        print('Valid phone number')
    else:
        print('Invalid phone number')


if __name__ == '__main__':
    check_phone('+375(29)328-22-36')
    check_phone('+375(29)-328-22-336')
