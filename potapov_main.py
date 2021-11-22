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

    def __str__(self):
        return self.name + ' ' + self.count + ' ' + self.creator + ' ' + self.price + ' ' + self.size


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

    def save(self):
        file = open('text.txt', 'w')
        for sneaker in self.sneakers:
            file.write(str(sneaker) + '\n')

print("команды: \n-- exit - закончить работу \n-- 1 - добавить товар \n--2 -вывести корзину")

command_string = input("Введите команду")
product_list = Storage()

while command_string != "exit":
    if command_string == "1":
        name = input("Введите имя: \n")
        count = input("Введите кол-во товаров: \n")
        creator = input("Введите производителя: \n")
        price = input("Введите цену: \n")
        size = input("Введите размер: \n")
        product_list.add_sneaker((name, count, creator, price, size))
    if command_string == "2":
        name = input("Введите имя: \n")
        product_list.remove_sneaker_by_name((name))
    if command_string == "3":
        product_list.save()

    command_string = input("Введите команду")
