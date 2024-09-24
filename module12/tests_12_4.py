import unittest
import logging
from rt_with_exceptions import Runner


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            r = Runner("Атлет 1", -5)
            for i in range(10):
                r.walk()

            self.assertEqual(r.distance, 50)

            logging.info('"test_walk" выполнен успешно')
        except ValueError as err:
            logging.warning('Неверная скорость для Runner', exc_info=True)
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            r = Runner(123)
            for i in range(10):
                r.run()

            self.assertEqual(r.distance, 100)

            logging.info('"test_run" выполнен успешно')
        except TypeError as err:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        w = Runner("Атлет 1")
        r = Runner("Атлет 2")
        for i in range(10):
            w.walk()
            r.run()

        self.assertNotEqual(w.distance, r.distance)


logging.basicConfig(level=logging.INFO, filemode="w", filename="./runner_tests.log", encoding='utf-8',
                        format="%(asctime)s | %(levelname)s | %(message)s")
    #unittest.main()

# Цель: получить опыт использования простейшего логирования совместно с тестами.
#
# Задача "Логирование бегунов":
# В первую очередь скачайте исходный код, который нужно обложить тестами с GitHub. (Можно скопировать)
# Основное обновление - выбрасывание исключений, если передан неверный тип в name и если передано отрицательное значение в speed.
#
# Для решения этой задачи вам понадобиться класс RunnerTest из предыдущей задачи.
# В модуле tests_12_4.py импортируйте пакет logging и настройте basicConfig на следующие параметры:
#
#     Уровень - INFO
#     Режим - запись с заменой('w')
#     Название файла - runner_tests.log
#     Кодировка - UTF-8
#     Формат вывода - на своё усмотрение, обязательная информация: уровень логирования, сообщение логирования.
#
#
# Дополните методы тестирования в классе RunnerTest следующим образом:
# test_walk:
#
#     Оберните основной код конструкцией try-except.
#     При создании объекта Runner передавайте отрицательное значение в speed.
#     В блок try добавьте логирование INFO с сообщением '"test_walk" выполнен успешно'
#     В блоке except обработайте исключение соответствующего типа и логируйте его на уровне WARNING с сообщением "Неверная скорость для Runner".
#
# test_run:
#
#     Оберните основной код конструкцией try-except.
#     При создании объекта Runner передавайте что-то кроме строки в name.
#     В блок try добавьте логирование INFO с сообщением '"test_run" выполнен успешно'
#     В блоке except обработайте исключение соответствующего типа и логируйте его на уровне WARNING с сообщением "Неверный тип данных для объекта Runner".