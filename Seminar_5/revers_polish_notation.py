input_string = input('Введите свое выражение: ')

if input_string.isdigit():
    input_string = [i for i in input_string]
else: 
    print('Вы ввели не число!!!')
    exit()
reverse_polish_notation = []

output_string = []

result = []

# Алгоритм обратной Польской записи
for elem in input_string:
    if elem.isdigit():
        output_string.append(elem)
    elif elem == "(":
        reverse_polish_notation.append(elem)
    elif elem == ")":
        while reverse_polish_notation and reverse_polish_notation[-1] != "(":
            output_string.append(reverse_polish_notation.pop())
        reverse_polish_notation.pop()
    elif elem == "*" or elem == "/":
        while reverse_polish_notation and reverse_polish_notation[-1] in ["*", "/"]:
            output_string.append(reverse_polish_notation.pop())
        reverse_polish_notation.append(elem)
    elif elem == "+" or elem == "-":
        while reverse_polish_notation and reverse_polish_notation[-1] in ["+", "-", "*", "/"]:
            output_string.append(reverse_polish_notation.pop())
        reverse_polish_notation.append(elem)
while reverse_polish_notation:
    output_string.append(reverse_polish_notation.pop())


# Сам калькулятор на основе алгоритма 
for i in output_string:
    if i.isdigit():
        result.append(int(i))
    elif i in ["+", "-", "*", "/"]:
        a = result.pop()
        b = result.pop()
        if i == "+":
            result.append(a + b)
        elif i == "-":
            result.append(a - b)
        elif i == "*":
            result.append(a * b)
        elif i == "/":
            result.append(a / b)

print(f'Ответ: {str(result)[1: -1]}')
