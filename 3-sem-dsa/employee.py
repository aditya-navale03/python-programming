class employees:
    employee1 = {
    "emp_no": 67,
    "emp_name": "Bob",
    "emp_desg": "Ethical Hacker",  
    "emp_salary": 120000,
}

    employee2 = {
    "emp_no": 68,
    "emp_name": "Alice",
    "emp_desg": "Software Engineer",
    "emp_salary": 95000,
}

    employee3 = {
    "emp_no": 69,
    "emp_name": "Charlie",
    "emp_desg": "Data Analyst",
    "emp_salary": 80000,
}

    employee4 = {
    "emp_no": 70,
    "emp_name": "David",
    "emp_desg": "Product Manager",
    "emp_salary": 110000,
}

    employee5 = {
    "emp_no": 71,
    "emp_name": "Eve",
    "emp_desg": "UX Designer",
    "emp_salary": 85000,
}

s = employees()
for emp in [s.employee1, s.employee2, s.employee3, s.employee4, s.employee5]:
    print(f"Employee No: {emp['emp_no']}")
    print(f"Employee Name: {emp['emp_name']}")
    print(f"Employee Designation: {emp['emp_desg']}")
    print(f"Employee Salary: {emp['emp_salary']}\n")