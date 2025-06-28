## task 1
import math as m
class Vector:
    x: int
    y: int
    z: int
    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z
    
    def magnitude(self):
        return m.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)
    
    def normalize(self):
        return Vector(
            self.x / self.magnitude(),
            self.y / self.magnitude(),
            self.z / self.magnitude()
        )

    def __str__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
    def __mul__(self, other):
        if type(other) is int:
            return Vector(
                self.x * other,
                self.y * other,
                self.z * other
            )
        elif type(other) is Vector:
            return self.x * other.x + self.y * other.y + self.z * other.z
        else:
            raise TypeError("can't multiply Vector and " + type(other).__name__)
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

# Print the vector
print(v1)          # Output: Vector(1, 2, 3)

# Addition
v3 = v1 + v2
print(v3)          # Output: Vector(5, 7, 9)

# Subtraction
v4 = v2 - v1
print(v4)          # Output: Vector(3, 3, 3)

# Dot product
dot_product = v1 * v2
print(dot_product) # Output: 32

# Scalar multiplication
v5 = v1 * 3
print(v5)          # Output: Vector(3, 6, 9)

# Magnitude
print(v1.magnitude())  # Output: 3.7416573867739413

# Normalization
v_unit = v1.normalize()
print(v_unit)      

## task 2
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


## task 3
# task3.py
from task import Task
from storage.csv_storage import CSVStorage
from storage.json_storage import JSONStorage

def choose_storage():
    choice = input("Choose storage format (1 = CSV, 2 = JSON): ")
    if choice == '1':
        return CSVStorage('tasks.csv')
    else:
        return JSONStorage('tasks.json')

def display_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    for task in tasks:
        print(f"{task.task_id}, {task.title}, {task.description}, {task.due_date}, {task.status}")

def main():
    storage = choose_storage()
    tasks = storage.load_tasks()

    while True:
        print("\nWelcome to the To-Do Application!")
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. Update a task")
        print("4. Delete a task")
        print("5. Filter tasks by status")
        print("6. Save tasks")
        print("7. Load tasks")
        print("8. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            task = Task(
                task_id=input("Enter Task ID: "),
                title=input("Enter Title: "),
                description=input("Enter Description: "),
                due_date=input("Enter Due Date (YYYY-MM-DD): "),
                status=input("Enter Status (Pending/In Progress/Completed): ")
            )
            tasks.append(task)
            print("Task added successfully!")

        elif choice == '2':
            display_tasks(tasks)

        elif choice == '3':
            task_id = input("Enter Task ID to update: ")
            for task in tasks:
                if task.task_id == task_id:
                    task.title = input("New Title: ")
                    task.description = input("New Description: ")
                    task.due_date = input("New Due Date: ")
                    task.status = input("New Status: ")
                    print("Task updated.")
                    break
            else:
                print("Task not found.")

        elif choice == '4':
            task_id = input("Enter Task ID to delete: ")
            tasks = [t for t in tasks if t.task_id != task_id]
            print("Task deleted if it existed.")

        elif choice == '5':
            status = input("Enter status to filter by: ")
            filtered = [t for t in tasks if t.status.lower() == status.lower()]
            display_tasks(filtered)

        elif choice == '6':
            storage.save_tasks(tasks)
            print("Tasks saved.")

        elif choice == '7':
            tasks = storage.load_tasks()
            print("Tasks loaded.")

        elif choice == '8':
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()


# task.py
from dataclasses import dataclass, asdict
from typing import Optional

@dataclass
class Task:
    task_id: str
    title: str
    description: str
    due_date: Optional[str]
    status: str

    def to_dict(self):
        return asdict(self)

    @staticmethod
    def from_dict(data: dict):
        return Task(**data)


#./storage/base_storage.py
from abc import ABC, abstractmethod
from typing import List
from task import Task

class BaseStorage(ABC):
    @abstractmethod
    def load_tasks(self) -> List[Task]:
        pass

    @abstractmethod
    def save_tasks(self, tasks: List[Task]):
        pass

#./storage/csv_storage.py
import csv
from typing import List
from task import Task
from storage.base_storage import BaseStorage

class CSVStorage(BaseStorage):
    def __init__(self, filename: str):
        self.filename = filename

    def load_tasks(self) -> List[Task]:
        tasks = []
        try:
            with open(self.filename, newline='', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    tasks.append(Task.from_dict(row))
        except FileNotFoundError:
            pass
        return tasks

    def save_tasks(self, tasks: List[Task]):
        with open(self.filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=Task.__annotations__.keys())
            writer.writeheader()
            for task in tasks:
                writer.writerow(task.to_dict())

#./storage/json_storage.py
import json
from typing import List
from task import Task
from storage.base_storage import BaseStorage

class JSONStorage(BaseStorage):
    def __init__(self, filename: str):
        self.filename = filename

    def load_tasks(self) -> List[Task]:
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return [Task.from_dict(task) for task in data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_tasks(self, tasks: List[Task]):
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump([task.to_dict() for task in tasks], f, indent=4)


