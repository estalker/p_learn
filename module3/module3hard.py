data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello",
                  ((), [{(2, 'Urban', ('Urban2', 35))}])]


def sum_any_type(s: int, *args):
    for i in args:
        if isinstance(i, str):
            s = s + len(i)
        elif isinstance(i, int):
            s = s + i
        elif isinstance(i, list):
            s = sum_any_type(s, *i)
        elif isinstance(i, dict):
            s = sum_any_type(s, *i.keys())
            s = sum_any_type(s, *i.values())
        elif isinstance(i, tuple):
            s = sum_any_type(s, *i)
        elif isinstance(i, set):
            s = sum_any_type(s, *i)
        else:
            raise RuntimeError('Unknown type')

    return s


print(sum_any_type(0, data_structure))
