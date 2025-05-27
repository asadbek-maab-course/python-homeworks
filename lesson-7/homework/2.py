class Employee:
    file = '/media/asadbek/D/maab/new/python-homeworks/lesson-6/homework/employees.txt'
    id = 2

    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

        with open(Employee.file, 'a') as f:
            f.write('\n' + ', '.join(
                    [str(Employee.id + 1), name, position, str(salary)]
                )
            )
        Employee.id += 1
        print("------ EMPLOYEE CREATED ------\n")
    
    @classmethod
    def getall(cls):
        print("------ VIEW ALL ------")
        with open(cls.file, 'r') as f:
            for line in f.readlines():
                print(line, end='')
        print("----------------------\n")
    
    @classmethod
    def search(cls, eid):
        eid = str(eid)
        with open(cls.file, 'r') as f:
            for line in f.readlines():
                if line[:line.index(',')] == eid:
                    return Employee()
        return "EMPLOYEE NOT FOUND"


Employee.getall()