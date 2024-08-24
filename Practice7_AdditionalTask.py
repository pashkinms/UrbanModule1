grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]

students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

student_list = sorted(list(students))
print(student_list)
journal = dict()
i = 0
while i<5:
    journal[student_list[i]] = sum(grades[i])/len(grades[i])
    i+=1
print(journal)