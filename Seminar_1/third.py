def quarter(x, y):
    if x > 0 and y > 0:
        print('1 четверть')
    elif x < 0 and y > 0:
        print('2 четверть')
    elif x < 0 and y < 0:
        print('3 четверть')
    else:
        print('4 четверть')
        

x = float(input('Введите значение \'X\': '))
y = float(input('Введите значение \'Y\': '))

if x == 0 or y == 0:
    print('X или Y не должны равняться нулю!!')

quarter(x, y)
