def calculateAvg(marks) :
    sum = 0
    sub = 0
    for mark in marks :
        sum += mark
        sub += 1
    avg = sum/sub
    return avg
    
students = [
    ("Alice", [85, 90, 78, 92]),
    ("Bob", [60, 65, 70, 75]),
    ("Charlie", [40, 45, 50, 55]),
    ("David", [95, 100, 98, 92])
]

dict = {}
for student in students:
    dict[student[0]] = student[1]

print("Dictionary of students and their grades:")
print(dict)

name = input("Enter student name for finding average :")
print("Avergae grage for",name, calculateAvg(dict[name]))
max_name = ""
max_avg = 0
count_passed = 0
for student in students :
    avg = calculateAvg(student[1])
    if avg > max_avg :
        max_avg = avg
        max_name = student[0]
    if avg > 50 :
        count_passed += 1

print("Student with the highest average grade:",max_name)
print("Number of students who passed:",count_passed)