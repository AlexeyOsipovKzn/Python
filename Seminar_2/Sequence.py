def digit_check():
    try:
        N = int(input('Введите число N: '))
        res, suma = sequence(N)
        print(f'Для N = {N}:  {res} --> Сумма = {suma}')
    except ValueError:
        print('Это не число !!!')
        digit_check()


def sequence(number):
    result = {}
    sum = 0
    for i in range(1, number + 1):
        result[i] = round((1 + (1 / i)) ** i, 1)
        sum += result[i]
    return result, sum


digit_check()
