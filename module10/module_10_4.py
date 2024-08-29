import random
import time
from threading import Thread
import queue


class Guest(Thread):
    def __init__(self, name: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name

    def run(self):
        time.sleep(random.randint(3, 10))


class Table:
    def __init__(self, number: int, guest: Guest = None):
        self.number = number
        self.guest = guest


class Cafe:
    def __init__(self, *tables):
        self.tables = tables
        self.queue = queue.Queue()

    def guest_arrival(self, *guests):
        for i, g in enumerate(guests):
            vacant = next((t for t in tables if t.guest is None), None)
            if vacant is None:
                self.queue.put(g)
                print(f"{g.name} в очереди")
            else:
                vacant.guest = g
                print(f"{g.name} сел(-а) за стол номер {vacant.number}")

    def discuss_guests(self):
        while not self.queue.empty() or any(t.guest is not None for t in self.tables):
            for i, t in enumerate(self.tables):
                if t.guest is not None and not t.guest.is_alive():
                    print(f"{t.guest.name} за текущим столом> покушал(-а) и ушёл(ушла)")
                    t.guest = None
                    print(f"Стол номер {t.number} свободен")

                if not self.queue.empty() and t.guest is None:
                    t.guest = self.queue.get()
                    print(f"{t.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {t.number}")
                    t.guest.start()


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman', 'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya',
                'Alexandra']
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()

# Задача "Потоки гостей в кафе":
# Необходимо имитировать ситуацию с посещением гостями кафе.
# Создайте 3 класса: Table, Guest и Cafe.
# Класс Table:
#
#     Объекты этого класса должны создаваться следующим способом - Table(1)
#     Обладать атрибутами number - номер стола и guest - гость, который сидит за этим столом (по умолчанию None)
#
# Класс Guest:
#
#     Должен наследоваться от класса Thread (быть потоком).
#     Объекты этого класса должны создаваться следующим способом - Guest('Vasya').
#     Обладать атрибутом name - имя гостя.
#     Обладать методом run, где происходит ожидание случайным образом от 3 до 10 секунд.
#
# Класс Cafe:
#
#     Объекты этого класса должны создаваться следующим способом - Cafe(Table(1), Table(2),....)
#     Обладать атрибутами queue - очередь (объект класса Queue) и tables - столы в этом кафе (любая коллекция).
#     Обладать методами guest_arrival (прибытие гостей) и discuss_guests (обслужить гостей).
#
# Метод guest_arrival(self, *guests):
#
#     Должен принимать неограниченное кол-во гостей (объектов класса Guest).
#     Далее, если есть свободный стол, то садить гостя за стол (назначать столу guest), запускать поток гостя и выводить на экран строку "<имя гостя> сел(-а) за стол номер <номер стола>".
#     Если же свободных столов для посадки не осталось, то помещать гостя в очередь queue и выводить сообщение "<имя гостя> в очереди".
#
# Метод discuss_guests(self):
# Этот метод имитирует процесс обслуживания гостей.
#
#     Обслуживание должно происходить пока очередь не пустая (метод empty) или хотя бы один стол занят.
#     Если за столом есть гость(поток) и гость(поток) закончил приём пищи(поток завершил работу - метод is_alive), то вывести строки "<имя гостя за текущим столом> покушал(-а) и ушёл(ушла)" и "Стол номер <номер стола> свободен". Так же текущий стол освобождается (table.guest = None).
#     Если очередь ещё не пуста (метод empty) и стол один из столов освободился (None), то текущему столу присваивается гость взятый из очереди (queue.get()). Далее выводится строка "<имя гостя из очереди> вышел(-ла) из очереди и сел(-а) за стол номер <номер стола>"
#     Далее запустить поток этого гостя (start)
#
# Таким образом мы получаем 3 класса на основе которых имитируется работа кафе:
#
#     Table - стол, хранит информацию о находящемся за ним гостем (Guest).
#     Guest - гость, поток, при запуске которого происходит задержка от 3 до 10 секунд.
#     Cafe - кафе, в котором есть определённое кол-во столов и происходит имитация прибытия гостей (guest_arrival) и их обслуживания (discuss_guests).
