def OneToN(number):
    numberList = []
    index = 1
    for i in range(1, number + 1):
        numberList.append(i * index)
        index = numberList[i - 1]
    return numberList


def digit_check():
    try:
        N = int(input('Введите число N: '))
        print(f'Пусть N = {N}, тогда  {OneToN(N)}')
    except ValueError:
        print('Это не число !!!')
        digit_check()


digit_check()