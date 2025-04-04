employees = [
    {"name": "Alice", "salary": 50000, "rating": 5},
    {"name": "Bob", "salary": 40000, "rating": 3},
    {"name": "Charlie", "salary": 35000, "rating": 2}
]

empUpdated = list(map(lambda employee : {
    "name" : employee["name"],
    "salary" : round(employee["salary"] * (1.1 if employee["rating"] >= 4 else (1.05 if employee["rating"] == 3 else 0.95))),
    "rating" : employee["rating"]
} ,employees))

print(empUpdated)