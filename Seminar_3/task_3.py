import random


def digit_check():
    try:
        numb = int(input('Введите колличество чисел в списке: '))
        min_max(numb)
    except ValueError:
        print('Это не число !!!')
        digit_check()


def min_max(number):
    result = []
    for i in range(number):
        result.append(round(random.uniform(1,20),2))
    total = [round(i % 1, 2) for i in result if i % 1 != 0]
    print(f'{result} => {max(total) - min(total)}')

digit_check()