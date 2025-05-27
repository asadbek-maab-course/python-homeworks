class Employee:
    id = 2

    def __init__(self, name, position, salary, eid = None):
        self.name = name
        self.position = position
        self.salary = salary
        self.eid = eid
    
    def to_line(self):
        return ", ".join([self.eid, self.name, self.position, self.salary])
    
    @classmethod
    def line_to_obj(cls, line):
        eid, name, position, salary = map(str, line.replace('\n', '').split(', '))
        return Employee(name, position, salary, eid)


    def __str__(self):
        return f"Employee({self.eid}, {self.name}, {self.position}, {self.salary})"

class EmployeeManager:
    def __init__(self, file = '/media/asadbek/D/maab/new/python-homeworks/lesson-7/homework/employees.txt'):
        self.file = file

    def add_new(self):
        name = input('Name: ')
        position = input('Position: ')
        salary = input('Salary: ')
        new_employe = Employee(name, position, salary)
        with open(Employee.file, 'a') as f:
            f.write('\n' + ', '.join(
                    [str(Employee.id + 1), name, position, str(salary)]
                )
            )
        Employee.id += 1
        print("------ EMPLOYEE CREATED ------\n")

    def getall(cls):
        print("------ VIEW ALL ------")
        with open(cls.file, 'r') as f:
            for line in f.readlines():
                print(line, end='')
        print("----------------------\n")

    def search(cls, eid):
        eid = str(eid)
        with open(cls.file, 'r') as f:
            for line in f.readlines():
                if line[:line.index(',')] == eid:
                    return Employee.line_to_obj(line)
        return "EMPLOYEE NOT FOUND"

print(EmployeeManager().search(2))