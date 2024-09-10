import sys


def introspection_info(obj):
    result = {"type": type(obj), "attributes": [], "methods": []}
    for att in dir(obj):
        if callable(getattr(obj, att)):
            result["methods"].append(att)
        else:
            result["attributes"].append(att)
    result["module"] = sys.modules[__name__]
    return result


number_info = introspection_info(42)
print(number_info)


# Необходимо создать функцию, которая принимает объект (любого типа) в качестве аргумента и проводит интроспекцию этого объекта, чтобы определить его тип, атрибуты, методы, модуль, и другие свойства.
#
# 1. Создайте функцию introspection_info(obj), которая принимает объект obj.
# 2. Используйте встроенные функции и методы интроспекции Python для получения информации о переданном объекте.
# 3. Верните словарь или строки с данными об объекте, включающий следующую информацию:
#   - Тип объекта.
#   - Атрибуты объекта.
#   - Методы объекта.
#   - Модуль, к которому объект принадлежит.
#   - Другие интересные свойства объекта, учитывая его тип (по желанию).