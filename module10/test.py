class T:
    def __init__(self, number: int):
        self.number = number


a = [T(1),T(2),T(3),T(4),T(5),T(6),T(7),T(8)]
first_match = next((x for x in a if x.number==8), None)
print(first_match)