"""
Groupby - intertools em Python
"""
import itertools 

employees = [
    ("Vera", "IT"),
    ("Chuck", "IT"),
    ("Dave", "ADMIN"),
    ("Karl", "IT"),
    ("Janet", "ADMIN"),
    ("Jack", "IT")
]

# IT: Chuck, Dave, Karl, Jack
# ADMIN: Vera, Janet


grouped_by_department = itertools.groupby(employees, lambda x: x[1])
for i, j in grouped_by_department:
    print(i, list(j))