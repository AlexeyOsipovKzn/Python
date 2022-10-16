from random import randint
import itertools


def get_ratios(k):
    ratios = [randint(0, 10) for i in range(k + 1)]
    while ratios[0] == 0:
        ratios[0] = randint(1, 10)
    return ratios


def get_polynomial(k, ratios):
    first = ['*x^']*(k-1) + ['*x']
    polynomial = [[a, b, c] for a, b, c in itertools.zip_longest(
        ratios, first, range(k, 1, -1), fillvalue='') if a != 0]
    for x in polynomial:
        x.append(' + ')
    polynomial = list(itertools.chain(*polynomial))
    polynomial[-1] = ' = 0'
    return "".join(map(str, polynomial)).replace(' 1*x', ' x')


num = input('Введите степень К:  ')
if num.isdigit() == True:
    print(get_polynomial(int(num), get_ratios(int(num))))
else:
    print('Это не число')


k = randint(1, 10)
first = get_polynomial(k, get_ratios(k))
with open(str('first.txt'), 'w') as data:
    data.write(first)


second = get_polynomial(k, get_ratios(k))
with open(str('second.txt'), 'w') as data:
    data.write(second)
