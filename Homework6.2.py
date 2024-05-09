from numpy import mean
magazine = {}
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = ['Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron']
my_list = list(students)
res = my_list.sort()
magazine = dict(zip(my_list, grades))
magazine: dict = {name: mean(values) for name, values in magazine.items()}
print(magazine)