import random


def digit_check():
    try:
        numb = int(input('Введите колличество чисел в списке: '))
        list_multiplying(numb)
    except ValueError:
        print('Это не число !!!')
        digit_check()


def list_multiplying(number):
    random_list = []
    multiply_list = []
    num = number
    for i in range(number):
        random_list.append(random.randint(1, 15))
    for index in range(len(random_list)):
        while index < len(random_list)/2 and num > len(random_list)/2:
            num -= 1
            multiply_list.append(random_list[index] * random_list[num])
            index += 1
    print(f'{random_list} --> {multiply_list}')


digit_check()
