from threading import Thread, Lock
from time import sleep

LOCK = Lock()


def do_print(msg):
    with LOCK:
        print(msg)


class Knight(Thread):
    number_of_foes = 100

    def __init__(self, name: str, power: int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.power = power

    def run(self):
        days = 0
        do_print(f"{self.name} на нас напали!")
        for i in range(Knight.number_of_foes, 0, -self.power):
            days = days + 1
            sleep(1)
            do_print(f"{self.name} сражается {days} день(дня)..., осталось {i - self.power} воинов.")
        do_print(f"{self.name}  одержал победу спустя {days} дней(дня)")


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

threads = [first_knight, second_knight]

for t in threads:
    t.start()

for t in threads:
    t.join()

print("Все битвы закончились!")

# Задача "За честь и отвагу!":
# Создайте класс Knight, наследованный от Thread, объекты которого будут обладать следующими свойствами:
#
#     Атрибут name - имя рыцаря. (str)
#     Атрибут power - сила рыцаря. (int)
#
# А также метод run, в котором рыцарь будет сражаться с врагами:
#
#     При запуске потока должна выводится надпись "<Имя рыцаря>, на нас напали!".
#     Рыцарь сражается до тех пор, пока не повергнет всех врагов (у всех потоков их 100).
#     В процессе сражения количество врагов уменьшается на power текущего рыцаря.
#     По прошествию 1 дня сражения (1 секунды) выводится строка "<Имя рыцаря> сражается <кол-во дней>..., осталось <кол-во воинов> воинов."
#     После победы над всеми врагами выводится надпись "<Имя рыцаря> одержал победу спустя <кол-во дней> дней(дня)!"
#
# Как можно заметить нужно сделать задержку в 1 секунду, инструменты для задержки выберите сами.
# Пункты задачи:
#
#     Создайте класс Knight с соответствующими описанию свойствами.
#     Создайте и запустите 2 потока на основе класса Knight.
#     Выведите на экран строку об окончании битв.
