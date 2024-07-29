import os


class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        if not os.path.exists(Shop.__file_name):
            open(Shop.__file_name, 'w').close()
        f = open(Shop.__file_name, "r")
        text = f.read()
        f.close()
        return text

    def add(self, *products):
        if not os.path.exists(Shop.__file_name):
            open(Shop.__file_name, 'w').close()
        f = open(self.__file_name, "r")
        lines = f.readlines()
        f.close()

        new_products = []
        for p in products:
            if isinstance(p, Product):
                if any(s.lower().startswith(p.name.lower() + ", ") for s in lines):
                    print(f'Продукт {p.name} уже есть в магазине')
                else:
                    new_products.append(p.__str__())

        fw = open(Shop.__file_name, "a")
        fw.write("\n".join(new_products))
        fw.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())

# Цель: закрепить знания о работе с файлами (чтение/запись) решив задачу.
#
# Задача "Учёт товаров":
# Необходимо реализовать 2 класса Product и Shop, с помощью которых будет производиться запись в файл с продуктами.
# Объекты класса Product будут создаваться следующим образом - Product('Potato', 50.0, 'Vagetables') и обладать следующими свойствами:
#
#     Атрибут name - название продукта (строка).
#     Атрибут weight - общий вес товара (дробное число) (5.4, 52.8 и т.п.).
#     Атрибут category - категория товара (строка).
#     Метод __str__, который возвращает строку в формате '<название>, <вес>, <категория>'. Все данные в строке разделены запятой с пробелами.
#
#
# Объекты класса Shop будут создаваться следующим образом - Shop() и обладать следующими свойствами:
#
#     Инкапсулированный атрибут __file_name = 'products.txt'.
#     Метод get_products(self), который считывает всю информацию из файла __file_name, закрывает его и возвращает единую строку со всеми товарами из файла __file_name.
#     Метод add(self, *products), который принимает неограниченное количество объектов класса Product. Добавляет в файл __file_name каждый продукт из products, если его ещё нет в файле (по названию). Если такой продукт уже есть, то не добавляет и выводит строку 'Продукт <название> уже есть в магазине' .
