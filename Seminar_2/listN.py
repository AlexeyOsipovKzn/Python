import random


def digit_check():
    try:
        number = int(input('Введите число N:  '))
        result, mult = listN(number)
        print(f'{result} Проиведение = {mult}')
    except ValueError:
        print('Это не число !!!')
        digit_check()


def listN(num):
    result = []
    file = []
    multiply = 1
    for i in range(num):
        result.append(random.randint(-num, num))

    product = open('file.txt', 'r')
    # Считываем и добавляем в список числа из file.txt
    for line in product:
        file.append(int(line))
    # Считаем произведение указанных позиций в file.txt
    for j in file:
        multiply *= result[j]
    return result, multiply


digit_check()
