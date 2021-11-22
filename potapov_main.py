class Sneaker:
    name = ''
    count = 0
    creator = ''
    price = 0
    size = ''

    def __init__(self, name, count, creator, price, size):
        self.name = name
        self.count = count
        self.creator = creator
        self.price = price
        self.size = size


class Storage:
    sneakers = []

    def add_sneaker(self, name, count, creator, price, size):

        for item in self.sneakers:
            if item.name == name and item.creator == creator and item.size == size:
                item.count += count
                item.price = price
                return

        self.sneakers.append(Sneaker(name, count, creator, price, size))

    def remove_sneaker_by_name(self, name):
        for item in self.sneakers:
            if item.name == name:
                self.sneakers.pop(name)

print("команды: \n-- exit - закончить работу \n-- 1 - добавить товар \n--2 -вывести корзину")

command_string = input("Введите команду")
product_list = {}

while command_string != "exit":
    if command_string == "1":
        name = input("Введите имя")
        count = input("Введите кол-во товаров")
        creator = input("Введите производителя")
        price = input("Введите цену")
        size = input("Введите размер")
        if name in product_list:
            product_list[name] = count
        else:
            product_list[name] = count
    if command_string == "2":
        print(product_list)

    command_string = input("Введите команду")
