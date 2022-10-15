import random


def non_repeating_list(number):
    result = []
    for item in range(number):
        result.append(random.randint(-10, 10))
    print(f'Первичный список --> {result}')
    result = list(set(result))
    print(f'Список неповторяющихся элементов исходной последовательности')
    print('\t\t\t  |')
    print('\t\t\t  |')
    print('\t\t\t  V')
    print(f'\t\t     {result}')


num = input('Введите длинну списка -- >  ')
if num.isdigit() == True:
    non_repeating_list(int(num))
else:
    print('Это не число')
