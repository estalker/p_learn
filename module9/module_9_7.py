def is_prime(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        prime_bool = True
        for n in range(2, res - 1):
            if res % n == 0:
                prime_bool = False
                break

        if prime_bool:
            print("Простое")
        else:
            print("Составное")

        return res

    return wrapper


@is_prime
def sum_three(*args):
    if len(args) != 3:
        raise ValueError('Нужно ровно 3 параметра')

    if not all(isinstance(x, int) for x in args):
        raise ValueError('Все параметры должны быть числами')

    res = 0
    for a in args:
        res += a
    return res


result = sum_three(2, 3, 6)
print(result)

# Напишите 2 функции:
#
#     Функция, которая складывает 3 числа (sum_three)
#     Функция декоратор (is_prime), которая распечатывает "Простое", если результат 1ой функции будет простым числом и "Составное" в противном случае.
#
# Пример:
# result = sum_three(2, 3, 6)
# print(result)
#
# Результат консоли:
# Простое
# 11
#
# Примечания:
#
#     Не забудьте написать внутреннюю функцию wrapper в is_prime
#     Функция is_prime должна возвращать wrapper
#     @is_prime - декоратор для функции sum_three