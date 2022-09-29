import math
x1 = float(input('Введите координаты точки А, x =  '))
y1 = float(input('Введите координаты точки А, y =  '))
x2 = float(input('Введите координаты точки B, x =  '))
y2 = float(input('Введите координаты точки B, x =  '))

result = int(math.sqrt(((x2 - x1)** 2) + ((y2 - y1)** 2)) * 100) / 100

print('-->', result)
