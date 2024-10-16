grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
#
grad_ = [sum(grades[0]) / len(grades[0]),
         sum(grades[1]) / len(grades[1]), sum(grades[2]) / len(grades[2]),
         sum(grades[3]) / len(grades[3]), sum(grades[4]) / len(grades[4])]
print(grad_)
stud_sort = sorted(students)
print(stud_sort)
zip_ = zip(stud_sort, grad_)  # 1*
print(zip_)
dict_ = dict(zip_)
print(dict_)

# 1 - Функция zip() в Python используется для одновременной итерации по нескольким итерируемым объектам (например, спискам, кортежам, строкам) параллельно.
# Она создает итератор, который генерирует кортежи, состоящие из соответствующих элементов из каждого итерируемого объекта
