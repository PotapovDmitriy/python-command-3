import json
import sql_service as sql


def read_from_file(storage):
    with open("test.json", "r") as file:
        dict_json = json.load(file)
        products = dict_json["sneakers"]

        for product in products:
            storage.add_sneaker(product["name"], product["count"], product["creator"],
                                product["price"], product["size"], product["article"])


def save_to_file(json_str):
    if json_str is None:
        print("Нечего сохранять")
        return

    with open("test.json", "w") as file:
        json.dump(json_str, file)
    print("сохранено")


class Sneaker:
    name = ''
    count = 0
    creator = ''
    price = 0
    size = ''
    article = ''

    def __init__(self, name, count, creator, price, size, article):
        self.name = name
        self.count = int(count)
        self.creator = creator
        self.price = int(price)
        self.size = size
        self.article = article

    def to_json(self):
        return {"name": self.name,
                "count": self.count,
                "creator": self.creator,
                "price": self.price,
                "size": self.size,
                "article": self.article}

    def __str__(self):
        return self.name + ' ' + str(self.count) + ' ' + self.creator + ' ' + str(self.price) + ' ' + self.size


class Storage:
    sneakers = {}

    def add_sneaker(self, _name, _count, _creator, _price, _size):
        sql.add_sneaker(_name, _count, _creator, _price, _size)

        # if _article in self.sneakers.keys():
        #     self.sneakers[_article].count += int(_count)
        #     self.sneakers[_article].price = int(_price)
        #     return
        #
        # self.sneakers[_article] = Sneaker(_name, _count, _creator, _price, _size, _article)

    def remove_sneaker_by_name(self, _name):
        sql.delete_by_name(_name)
        # self.sneakers.pop(_name)

    def to_json(self):
        if self.sneakers is None:
            print("")
            return None

        sneakers_json_list = []
        for item in self.sneakers:
            sneakers_json_list.append(self.sneakers[item].to_json())
        return {"sneakers": sneakers_json_list}

    def display(self):
        sql.select_all()
        # if len(self.sneakers) == 0:
        #     print("Пусто")
        #     return
        #
        # for key in self.sneakers:
        #     print(f"{key} - {self.sneakers[key]} ")

#
product_list = Storage()
# read_from_file(product_list)

while True:
    print("команды: \n-- exit - закончить работу \n-- 1 - добавить товар \n-- 2 -вывести корзину"
          "\n-- 3 - удалить товар по артикулу \n-- 4 - сохранить в файл \n-- 5 - прочитать из файла ")
    command_string = input("Введите команду \n")

    if command_string == "exit":
        save_to_file(product_list)
        exit()
    if command_string == "1":
        print("Если артикул совпадает  другим товаром, то их кол-во просто просуммируется!!!")
        name = input("Введите имя: \n")
        count = input("Введите кол-во товаров: \n")
        creator = input("Введите производителя: \n")
        price = input("Введите цену: \n")
        size = input("Введите размер: \n")
        product_list.add_sneaker(name, count, creator, price, size)
    if command_string == "2":
        product_list.display()
    if command_string == "3":
        name = input("Введите имя: \n")
        product_list.remove_sneaker_by_name(name)
    if command_string == "4":
        save_to_file(product_list.to_json())
    if command_string == "5":
        read_from_file(product_list)
