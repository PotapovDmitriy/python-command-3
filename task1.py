sneakers = {}

while True:
    print('Что хотите сделать?\n'
          '1 - добавление\n'
          '2 - отображение всего')
    command = int(input())
    if command == 1:
        print('Введите название кроссовок:')
        sneakersName = input()
        print('Введите кол-во кроссовок:')
        sneakersCount = int(input())
        if sneakersName in sneakers:
            sneakers[sneakersName] += sneakersCount
        else:
            sneakers[sneakersName] = sneakersCount
        print('Добавлено')
    elif command == 2:
        print(sneakers)
    else:
        print('Не угадал')
