import sql_service as sql

while True:
    print("команды: \n-- exit - закончить работу \n-- 1 - добавить товар \n-- 2 - вывести корзину"
          "\n-- 3 - удалить товар по названию \n-- 4 - Добавить новый размер \n-- 5 - Добавиь нового производителя")
    command_string = input("Введите команду \n")

    if command_string == "exit":
        exit()
    if command_string == "1":
        print("Если наименование совпадает другим товаром, то их кол-во просто просуммируется!!!")
        name = input("Введите имя: \n")
        count = input("Введите кол-во товаров: \n")
        creators = sql.select_all_creators()
        creator = input(f"Введите производителя из списка ({[creator.name for creator in creators]}): \n")
        price = input("Введите цену: \n")
        sizes = sql.select_all_sizes()
        size = input(f"Введите размер из спсика({[size.value for size in sizes]}): \n")
        sql.add_sneaker(name, count, creator, price, size)
    if command_string == "2":
        sql.print_all_sneakers()
    if command_string == "3":
        name = input("Введите имя: \n")
        sql.delete_by_name(name)
    if command_string == "4":
        value = input("Введите значение размера: \n")
        sql.add_size(value)
    if command_string == "5":
        name = input("Введите название: \n")
        country = input("Введите страну производства: \n")
        sql.add_creator(name, country)
