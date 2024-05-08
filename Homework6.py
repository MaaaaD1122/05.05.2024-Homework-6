magazine = {}
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
#преобразование множества students в список
my_list = list(students)
#сортировка списка студентов в алфавитный порядок
res = my_list.sort()
#подсчёт среднего балла
count1 = sum(grades[0])
avg1 = count1 / len(grades[0])
count2 = sum(grades[1])
avg2 = count2 / len(grades[1])
count3 = sum(grades[2])
avg3 = count3 / len(grades[2])
count4 = sum(grades[3])
avg4 = count4 / len(grades[3])
count5 = sum(grades[4])
avg5 = count5 / len(grades[4])
grades1 = (avg1, avg2, avg3, avg4, avg5)
#внесение списков в словарь с помощью zip
magazine = dict(zip(my_list, grades1))
print(magazine)