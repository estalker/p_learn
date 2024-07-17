import house

h1 = house.House('ЖК Эльбрус', 10)
print(house.House.houses_history)
h2 = house.House('ЖК Акация', 20)
print(house.House.houses_history)
h3 = house.House('ЖК Матрёшки', 20)
print(house.House.houses_history)

# Удаление объектов
del h2
del h3

print(house.House.houses_history)
