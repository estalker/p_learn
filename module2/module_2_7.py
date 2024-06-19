def print_params(a = 1, b = 'строка', c = True):
    print(f'a={a} b={b} c={c}')

print_params()
print_params(b = 25)
print_params(c = [1,2,3])

values_list = [2, 'стро4ка', False]
values_dict = { 'a': 2, 'b': 'стро4ка', 'c': False }

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)