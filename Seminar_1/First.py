number = int(input())
if 0 <= number < 6:
    print(f'{number} -> Нет')
elif 6 <= number <= 7:
    print(f'{number} -> Да')
else:
    print(f'{number} -> Вне диапазона')
