def seq_id():
    f = open('/media/asadbek/D/maab/new/python-homeworks/lesson-7/homework/employees.txt', 'r')
    last = f.readlines()[-1].split(', ')[0]
    return int(last)

class Employee:
    id = seq_id()

    def __init__(self, name, position, salary, eid = None):
        self.name = name
        self.position = position
        self.salary = salary
        self.eid = eid
        if eid is None:
            self.eid = str(Employee.id + 1)
            Employee.id += 1
    
    def to_line(self):
        return ", ".join([self.eid, self.name, self.position, self.salary]) + "\n"
    
    @classmethod
    def line_to_obj(cls, line):
        eid, name, position, salary = map(str, line.replace('\n', ' ').split(', '))
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
        with open(self.file, 'a') as f:
            f.write(new_employe.to_line())
        print("------ EMPLOYEE CREATED ------\n")

    def getall(cls):
        print("------ VIEW ALL ------")
        with open(cls.file, 'r') as f:
            for line in f.readlines():
                print(line, end='')
        print("----------------------\n")

    def search(cls):
        eid = input('Enter employee id:')
        with open(cls.file, 'r') as f:
            for line in f.readlines():
                if line[:line.index(',')] == eid:
                    print(Employee.line_to_obj(line))
        print("EMPLOYEE NOT FOUND")

    def update(self):
        eid = input('Employee id:')
        name = input('Employee name:')
        position = input('Employee position:')
        salary = input('Employee salary:')
        text = ""
        is_updated = False
        with open(self.file, 'r') as f:
            for line in  f.readlines():
                if line.split(', ')[0] == str(eid):
                    is_updated = True
                    text += ', '.join([str(eid), name, position, str(salary)]) + "\n"
                    continue
                text += line
        if is_updated:
            print("------ EMPLOYEE DATA UPDATED ------\n")
            f = open(self.file, 'w')
            f.write(text)
            f.close()
        else:
            print(f"------ EMPLOYEE WITH {eid} ID NOT FOUND ------\n")


    def delete(self):
        eid = input("Enter employee id: ")
        text = ""
        with open(self.file, 'r') as f:
            for line in  f.readlines():
                if line.split(', ')[0] == str(eid):
                    continue
                text += line
        f = open(self.file, 'w')
        print("------ EMPLOYEE DELETED ------\n")
        f.write(text)
        f.close()
    
    def sort_by(self):
        col = input('Enter column for sort(id, name, salary): ')
        while not col in "id, name, salary":
            print("column does not exists. enter valid column or q for quit.")
            col = input('Enter column for sort(id, name, salary): ')
            if col == 'q':
                return
        employees = []
        with open(self.file, 'r') as f:
            for line in f.readlines():
                employees.append(Employee.line_to_obj(line))
        if col == 'id':
            employees.sort(key=lambda obj: obj.eid)
        elif col == 'name':
            employees.sort(key=lambda obj: obj.name)
        elif col == 'salary':
            employees.sort(key=lambda obj: obj.salary)
        
        print(f"------ SORTED BY - {col} ------")
        for empl in employees:
            print(empl)
        print("----------------------\n")
        
        
        

def hlp():
    print("h - help\n1 - create new employee\n2 - view all employees\n3 - update employee\n4 - delete employee\n5 - search by id\n6 - view custom order\nq - exit")

hlp()
while True:
    c = input(">> ")
    if c == "h":
        hlp()
    elif c == '1':
        EmployeeManager().add_new()
    elif c == '2':
        EmployeeManager().getall()
    elif c == '3':
        EmployeeManager().update()
    elif c == '4':
        EmployeeManager().delete()
    elif c == '5':
        EmployeeManager().search()
    elif c == '6':
        EmployeeManager().sort_by()
    elif c == 'q':
        break
    else:
        print("commant not found. type h for help")
