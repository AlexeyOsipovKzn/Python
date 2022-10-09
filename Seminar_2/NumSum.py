def numSum(num):
    sum = 0
    for i in str(num):
        if i != ".":
            sum += int(i)
    return sum

def digit_check():
    try:
        number = float(input('Введите число:  '))
        print(f'--> {numSum(number)}')
    except ValueError:
        print('Это не число !!!')
        digit_check()

digit_check()


