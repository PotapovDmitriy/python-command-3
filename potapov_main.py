print("команды: \n-- exit - закончить работу \n-- 1 - добавить товар \n--2 -вывести корзину")

command_string = input("Введите команду")
product_list = {}

while command_string != "exit":
    if command_string == "1":
        name = input("Введите имя")
        count = input("Введите кол-во товаров")
        if name in product_list:
            product_list[name] = count
        else:
            product_list[name] = count
    if command_string == "2":
        print(product_list)

    command_string = input("Введите команду")

