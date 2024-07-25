import  math
class Figure:
    def __init__(self, sides_count, color, sides, filled = False):
        self.sides_count = sides_count
        self.__color = color
        self.__sides = sides
        self.filled = filled

    def __is_valid_color(self, r: int, g: int, b: int):
        return 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255

    def get_color(self):
        return self.__color

    def set_color(self, r: int, g: int, b: int):
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)

    def get_sides(self):
        return self.__sides

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(new_sides):
            self.__sides = list(new_sides)

    def __len__(self):
        return sum(self.__sides)

    def __is_valid_sides(self, sides):
        if all(isinstance(x, int) and x > 0 for x in sides) and len(sides) == len(self.__sides):
            return True
        return False


class Circle(Figure):
    def __init__(self, color, size_of_edge):
        sides_count = 1
        self.__radius = size_of_edge / 2 / math.pi
        super().__init__(sides_count, color, [size_of_edge])

    def get_square(self):
        return math.pi * pow(self.__radius, 2)


class Triangle(Figure):
    def __init__(self, color, sides):
        sides_count = 3

        p = sum(sides) / 2
        sq = math.sqrt(p * (p - sides[0]) * (p - sides[1]) * (p - sides[2]))
        self.__height = [
            2 / sides[0] * sq,
            2 / sides[1] * sq,
            2 / sides[2] * sq
        ]
        super().__init__(sides_count, color, sides)

    def get_square(self):
        return self.__height * self.get_sides()[0] / 2


class Cube(Figure):
    def __init__(self, color, size_of_edge):
        sides_count = 12
        super().__init__(sides_count, color, [size_of_edge] * sides_count)

    def get_volume(self):
        return pow(self.get_sides()[0], 3)


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())


