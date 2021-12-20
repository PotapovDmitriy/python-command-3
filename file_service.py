import json


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
