def is_true(x, y, z):
    left = not (x or y or z)
    right = not x and not y and not z
    
    if left == right:
        print('Утверждение истинно')
    else:
        print('Утверждение ложно')

x = int(input('Введите зачение предиканта \'X\': '))
y = int(input('Введите зачение предиканта \'Y\': '))
z = int(input('Введите зачение предиканта \'Z\': '))

is_true(x, y, z)
