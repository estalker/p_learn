def all_variants(text):
    for first in range(0, len(text)):
        for last in range(first + 1, len(text) + 1):
            yield text[first:last]


a = all_variants("abc")
for i in a:
    print(i)

# Напишите функцию-генератор all_variants(text), которая принимает строку text и возвращает объект-генератор, при каждой итерации которого будет возвращаться подпоследовательности переданной строки.
#
# Пункты задачи:
#
#     Напишите функцию-генератор all_variants(text).
#     Опишите логику работы внутри функции all_variants.
#     Вызовите функцию all_variants и выполните итерации.
