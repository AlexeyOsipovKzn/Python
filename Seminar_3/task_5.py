def digit_check():
    try:
        numb = int(input('Введите число k: '))
        print(f'для k = {numb} список будет выглядеть так: {extend_and_sort(fibonacci(numb), negative_fibonacci(numb))}')
    except ValueError:
        print('Это не число !!!')
        digit_check()


def fibonacci(number):
    result = []
    fib1 = 1
    fib2 = 0
    index = 0
    while index < number:
        fib_sum = fib2 + fib1
        fib1 = fib2
        fib2 = fib_sum
        result.append(fib_sum)
        index += 1
    return(result)

def negative_fibonacci(number):
    result = []
    fib1 = 1
    fib2 = -1
    index = 0
    while index <= number:
        fib_sum = fib2 + fib1
        fib1 = fib2
        fib2 = fib_sum
        result.append(fib_sum)
        index += 1
    return(result)

def extend_and_sort(list1, list2):
    list1.extend(list2)
    list1.sort()
    return list1

digit_check()
