sneakers =  {}

def addStock(sneakersName, sneakersCount, sneakersManufacture, sneakersPrice, sneakersSize):

    sneakers[sneakersName] = list[sneakersCount, sneakersManufacture, sneakersPrice, sneakersSize]
    return sneakers

while True:
    print('Что хотите сделать?\n'
          '1 - добавление\n'
          '2 - отображение всего\n'
          '3 - удалить позицию\n'
          '4 - статистика по позициям\n')
    command = int(input())
    if command == 1:
        print('Введите название кроссовок:')
        sneakersName = input()
        print('Введите кол-во кроссовок:')
        sneakersCount = int(input())
        print('Введите производителя:')
        sneakersManufacture = str(input())
        print('Введите цену:')
        sneakersPrice = float(input())
        print('Введите размер:')
        sneakersSize = float(input())

        addStock(sneakersName, sneakersCount, sneakersManufacture, sneakersPrice, sneakersSize)

        #
        # if sneakersName in sneakers:
        #     sneakers[sneakersName] += sneakersCount
        # else:
        #     sneakers[sneakersName] = sneakersCount

        print(sneakers)



    elif command == 2:
        print(sneakers)


    elif command == 3:
        pass






    elif command == 4:
        print('Введите поле для подсчета статистики:')
        field = str(input())
        print(sneakers.count(field))
    else:
        print('Не угадал')
