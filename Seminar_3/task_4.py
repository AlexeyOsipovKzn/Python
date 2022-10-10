def digit_check():
    try:
        numb = int(input('Введите число: '))
        binary(numb)
    except ValueError:
        print('Это не число !!!')
        digit_check()

def binary(number):
    binary = format(number, "0b")
    print(f'{number} -> {binary}')

digit_check()