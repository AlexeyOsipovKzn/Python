import random


def shuffle(numbers):
    mix = []
    for i in range(numbers):
        mix.append(random.randint(-numbers, numbers))
    print(f'Первоначальный список --> {mix}')
    random.shuffle(mix)
    print(f'Перемешанный список --> {mix}')


def digit_check():
    try:
        numb = int(input('Введите число N: '))
        shuffle(numb)
    except ValueError:
        print('Это не число !!!')
        digit_check()

digit_check()