comands_list = ['1', '2']
foots = {}
while True:
    print('Для добавления товара введите цифу 1')
    print('Для просмотра всего введите цифу 2')
    command = input('Введите номер команды: ')
    if command not in comands_list:
        print('Неверна команда, попробуйте снова')
        continue
    elif command == '1':
        name = input('Введите название кросовок: ')
        count = int(input('Введите количество: '))
        if name in foots:
            foots[name] += count
        else:
            foots[name] = count
    else:
        print(foots)
