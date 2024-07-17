class House:
    houses_history = []
    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return super().__new__(cls)
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")
    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print("Такого этажа не существует")
            return
        for i in range(1, new_floor + 1):
            print(i)
    def __len__(self):
       return self.number_of_floors
    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}."

    @staticmethod
    def  getNumberOfFloors(obj):
        if isinstance(obj, House):
            return obj.number_of_floors
        elif isinstance(obj, int):
            return obj
        else:
            return 0

    def __eq__(self, other):
        return House.getNumberOfFloors(self) == House.getNumberOfFloors(other)
    def __lt__(self, other):
        return House.getNumberOfFloors(self) < House.getNumberOfFloors(other)
    def __le__(self, other):
        return House.getNumberOfFloors(self) <= House.getNumberOfFloors(other)
    def __gt__(self, other):
        return House.getNumberOfFloors(self) > House.getNumberOfFloors(other)
    def __ge__(self, other):
        return House.getNumberOfFloors(self) >= House.getNumberOfFloors(other)
    def __ne__(self, other):
        return House.getNumberOfFloors(self) != House.getNumberOfFloors(other)
    def __add__(self, other):
        self.number_of_floors = House.getNumberOfFloors(self) + House.getNumberOfFloors(other)
        return self
    def __radd__(self, value):
        return self.__add__(value)
    def __iadd__(self, value):
        return self.__add__(value)

