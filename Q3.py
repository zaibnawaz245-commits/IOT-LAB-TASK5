employees = []

for i in range(1, 4):
    name = input(f"Enter name of employee {i}: ")
    age = int(input(f"Enter age of employee {i}: "))
    salary = float(input(f"Enter salary of employee {i}: "))
    employee = (name, age, salary)
    employees.append(employee)

print("Employees List:", employees)
