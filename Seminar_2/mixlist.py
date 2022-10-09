import random

numbers = int(input('Введите число N: '))
mix = []
for i in range(numbers):
    mix.append(random.randint(-numbers, numbers))
print(f'Первоначальный список --> {mix}')
random.shuffle(mix)
print(f'Перемешанный список --> {mix}')