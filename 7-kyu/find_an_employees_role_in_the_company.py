# https://www.codewars.com/kata/55c9fb1b407024afe6000055

def find_employees_role(name):
    if ' ' not in name:
        return 'Does not work here!'
    for employee in employees:
        if (employee['first_name'],  employee['last_name']) == tuple(name.split(' ')):
            return employee['role']
    return 'Does not work here!'

