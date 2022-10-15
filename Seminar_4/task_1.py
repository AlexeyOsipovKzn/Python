import math
from decimal import Decimal

def precision(number):
    return Decimal(str(number)).as_tuple().exponent*(-1)


def is_float_digit(value) -> bool:
    try:
        float(value)
        return True
    except ValueError:
        return False


d = input('Введите точность d, пример (при d = 0.001, π = 3.141.):  ')
if is_float_digit(d) == True:
    print(f'при d = {d}, π = ' + '{:.{}f}'.format(math.pi, precision(d)))
else:
    print('Это не число')
