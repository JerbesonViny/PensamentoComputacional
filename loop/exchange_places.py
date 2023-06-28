number_of_students = int(input("Quantidade de alunos: "))
students = []

print("Digite os nomes dos alunos: ")

for i in range(number_of_students):
  student_name = input("")

  students.append(student_name)

if len(students) >= 4:
  for studentIdx in range(1, number_of_students-2, 2):
    oddIdx = studentIdx
    inverseOddIdx = -(studentIdx+1) if number_of_students % 2 != 0 else -studentIdx
    students[oddIdx], students[inverseOddIdx] = students[inverseOddIdx], students[oddIdx]

print('Nova lista:')
for student in students:
  print(student)
