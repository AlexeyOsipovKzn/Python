import random


def digit_check():
    try:
        numb = int(input('Введите колличество чисел в списке: '))
        uneven_sum(numb)
    except ValueError:
        print('Это не число !!!')
        digit_check()


def uneven_sum(number):
    random_list = []
    uneven_index = []
    sum = 0
    for i in range(number):
        random_list.append(random.randint(1, 50))
    for index, num in enumerate(random_list):
        if index % 2 != 0:
            sum += num
            uneven_index.append(num)
    filter_uneven_index = (str(uneven_index).strip('[]'))
    print(f'{random_list} -> на нечётных позициях элементы {filter_uneven_index}  ответ: {sum} ')


digit_check()
