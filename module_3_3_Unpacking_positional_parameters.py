def print_params(a = 1, b = 'строка', c = True):
    print(a)
    print(b)
    print(c)

print_params()
print_params(b = 25)
print_params(c = [1,2,3])

values_list = ["test", True, 4]
values_dict = {"a": 'test2', "b": 5, "c": False}
values_list_2 = ["test", 6]

print_params(**values_dict)
print_params(*values_list)
print_params(*values_list_2, 42)

print_params()