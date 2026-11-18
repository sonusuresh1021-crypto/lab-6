from employee import employee_details

def test_employee_details():
    result = employee_details("Rahul", "EMP101", "IT", "50000")

    assert result["Name"] == "Rahul"
    assert result["Employee ID"] == "EMP101"
    assert result["Department"] == "IT"
    assert result["Salary"] == "50000"
