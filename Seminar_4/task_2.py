import math


def prime_multipliers(number):
    index = 2
    multipliers = []
    while number >= index:
        if number % index == 0:
            number /= index
            multipliers.append(index)
        else:
            index += 1
    return multipliers

num = input('Введите натуральное число N:  ')
if num.isdigit() == True:
    print(f'Список простых множителей числа N = {prime_multipliers(int(num))}')
else:
    print('Это не число')
