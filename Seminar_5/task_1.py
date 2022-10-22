def del_words(name):
    words = name.split()
    result = []
    for item in words:
        if 'абв' not in item:
            result.append(item)
    print('Слова без содержания \"абв\" -- >', *result)


word = input('Введите слова через пробел:  ')
del_words(word)
