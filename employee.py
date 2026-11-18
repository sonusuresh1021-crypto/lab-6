def employee_details(name, emp_id, department, salary):
    return {
        "Name": name,
        "Employee ID": emp_id,
        "Department": department,
        "Salary": salary
    }


if __name__ == "__main__":
    import sys

    name = sys.argv[1]
    emp_id = sys.argv[2]
    department = sys.argv[3]
    salary = sys.argv[4]

    result = employee_details(name, emp_id, department, salary)

    print("Name:", result["Name"])
    print("Employee ID:", result["Employee ID"])
    print("Department:", result["Department"])
    print("Salary:", result["Salary"])
