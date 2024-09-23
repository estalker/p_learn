import unittest
from runner_and_tournament import Runner, Tournament


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        self.h = Runner("Усэйн", 10)
        self.a = Runner("Андрей", 9)
        self.n = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for i in cls.all_results:
            for j, entry in i.items():
                print(f"{j}:{entry}")
            print()

    def test_H_N(self):
        t = Tournament(5,self.n, self.h)
        all_results = t.start()
        self.all_results.append(all_results)
        last = max(all_results.keys())
        self.assertTrue(self.n == all_results[last])

    def test_A_N(self):
        t = Tournament(5,self.n, self.a)
        all_results = t.start()
        self.all_results.append(all_results)
        last = max(all_results.keys())

    def test_H_A_N(self):
        t = Tournament(5,self.n, self.a, self.h)
        all_results = t.start()
        self.all_results.append(all_results)
        last = max(all_results.keys())
        self.assertTrue(self.n == all_results[last])


if __name__ == "__main__":
    unittest.main()


# Задача:
# В первую очередь скачайте исходный код, который нужно обложить тестами с GitHub. (Можно скопировать)
# В этом коде сможете обнаружить дополненный с предыдущей задачи класс Runner и новый класс Tournament.
# Изменения в классе Runner:
#
#     Появился атрибут speed для определения скорости бегуна.
#     Метод __eq__ для сравнивания имён бегунов.
#     Переопределены методы run и walk, теперь изменение дистанции зависит от скорости.
#
# Класс Tournament представляет собой класс соревнований, где есть дистанция, которую нужно пробежать и список участников. Также присутствует метод start, который реализует логику бега по предложенной дистанции.
#
# Напишите класс TournamentTest, наследованный от TestCase. В нём реализуйте следующие методы:
#
# setUpClass - метод, где создаётся атрибут класса all_results. Это словарь в который будут сохраняться результаты всех тестов.
# setUp - метод, где создаются 3 объекта:
#
#     Бегун по имени Усэйн, со скоростью 10.
#     Бегун по имени Андрей, со скоростью 9.
#     Бегун по имени Ник, со скоростью 3.
#
# tearDownClass - метод, где выводятся all_results по очереди в столбец.
#
# Так же методы тестирования забегов, в которых создаётся объект Tournament на дистанцию 90. У объекта класса Tournament запускается метод start, который возвращает словарь в переменную all_results. В конце вызывается метод assertTrue, в котором сравниваются последний объект из all_results (брать по наибольшему ключу) и предполагаемое имя последнего бегуна.
# Напишите 3 таких метода, где в забегах участвуют (порядок передачи в объект Tournament соблюсти):
#
#     Усэйн и Ник
#     Андрей и Ник
#     Усэйн, Андрей и Ник.
#
# Как можно понять: Ник всегда должен быть последним.
#
# Дополнительно (не обязательно, не влияет на зачёт):
# В данной задаче, а именно в методе start класса Tournament, допущена логическая ошибка. В результате его работы бегун с меньшей скоростью может пробежать некоторые дистанции быстрее, чем бегун с большей.
# Попробуйте решить эту проблему и обложить дополнительными тестами.
# Пример результата выполнения тестов:
# Вывод на консоль:
# {1: Усэйн, 2: Ник}
# {1: Андрей, 2: Ник}
# {1: Андрей, 2: Усэйн, 3: Ник}
#
# Ran 3 tests in 0.001s
# OK
#
# Примечания:
#
#     Ваш код может отличаться от строгой последовательности описанной в задании. Главное - схожая логика работы тестов и наличие всех перечисленных переопределённых методов из класса TestCase.