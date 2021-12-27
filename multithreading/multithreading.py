from threading import Thread
import os
from datetime import datetime
import random


def create_and_write_file(number):
    with open(f'{path}{number}_text.txt', "w") as file:
        string_count = random.randint(20, 100)
        for string_number in range(string_count):
            numbers_count = random.randint(5, 40)

            for number in range(numbers_count):
                res = random.randint(0, 9)
                file.write(str(res))

            file.write('\n')


def read_and_sum_file(number):
    with open(f'{path}{number}_text.txt', "r") as file:
        text = file.read().replace("\n", '')
        res = 0
        for i in text:
            res = res + int(i)

        return res


def do_something_long(start, end):
    for i in range(start, end):
        create_and_write_file(i)

    for i in range(start, end):
        print(f"{i} : {read_and_sum_file(i)}")


flag = input() == "th"
count = int(input("Кол-во файлов в тыс. "))
start_time = datetime.now()

path = "../garbage/test/"
os.mkdir(path)
threads = []

if flag:
    for i in range(count):
        start = i * 1000
        threads.append(Thread(target=do_something_long, args=(start, start + 1000)))

    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
else:
    for i in range(count):
        start = i * 1000
        do_something_long(start, start + 1000)

print(datetime.now() - start_time)
