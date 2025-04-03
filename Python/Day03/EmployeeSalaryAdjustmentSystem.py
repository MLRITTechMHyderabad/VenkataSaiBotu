def updateSal(employee):
    if employee["rating"] >= 4 :
        employee["salary"] *= 1.1
    elif employee["rating"] == 3 :
        employee["salary"] *= 1.05
    else :
        employee["salary"] *= 0.95
    return employee

employees = [
    {"name": "Alice", "salary": 50000, "rating": 5},
    {"name": "Bob", "salary": 40000, "rating": 3},
    {"name": "Charlie", "salary": 35000, "rating": 2}
]

empUpdated = list(map(lambda employee : updateSal(employee) ,employees))

print(empUpdated)