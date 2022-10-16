import itertools
import re


file1 = 'first.txt'
file2 = 'second.txt'
file_sum = 'sum.txt'


def read(file):
    with open(str(file), 'r') as data:
        file = data.read()
    return file


def string_to_tuple(file):
    file = file.replace('= 0', '')
    file = re.sub("[*|^| ]", " ", file).split('+')
    file = [char.split(' ') for char in file]
    file = [[x for x in list if x] for list in file]
    for index in file:
        if index[0] == 'x':
            index.insert(0, 1)
        if index[-1] == 'x':
            index.append(1)
        if len(index) == 1:
            index.append(0)
    file = [tuple(int(x) for x in j if x != 'x') for j in file]
    return file


def sum_tuple(file_1, file_2):
    x = [0] * (max(file_1[0][1], file_2[0][1] + 1))
    for i in file_1 + file_2:
        x[i[1]] += i[0]
    result = [(x[i], i) for i in range(len(x)) if x[i] != 0]
    result.sort(key=lambda r: r[1], reverse=True)
    return result


def get_sum_polynomial(file):
    var = ['*x^'] * len(file)
    coefficient = [x[0] for x in file]
    rates = [x[1] for x in file]
    new_polynomial = [[str(a), str(b), str(c)]
                      for a, b, c in (zip(coefficient, var, rates))]
    for x in new_polynomial:
        if x[0] == '0':
            del (x[0])
        if x[-1] == '0':
            del (x[-1], x[-1])
        if len(x) > 1 and x[0] == '1' and x[1] == '*x^':
            del (x[0], x[0][0])
        if len(x) > 1 and x[-1] == '1':
            del x[-1]
            x[-1] = '*x'
        x.append(' + ')
    new_polynomial = list(itertools.chain(*new_polynomial))
    new_polynomial[-1] = ' = 0'
    return "".join(map(str, new_polynomial))


first = read(file1)
second = read(file2)
first_txt = string_to_tuple(first)
second_txt = string_to_tuple(second)
polynomial_sum = get_sum_polynomial(sum_tuple(first_txt, second_txt))
with open(file_sum, 'w') as data:
    data.write(polynomial_sum)

print(first)
print(second)
print(polynomial_sum)
