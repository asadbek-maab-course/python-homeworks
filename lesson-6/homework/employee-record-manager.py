def add_employee(name, position, salary):
    with open('/media/asadbek/D/maab/new/python-homeworks/lesson-6/homework/employees.txt', 'a') as f:
        f.write('\n' + ', '.join(
                [str(id(name + position + str(salary))), name, position, str(salary)]
            )
        )

def view():
    with open('/media/asadbek/D/maab/new/python-homeworks/lesson-6/homework/employees.txt', 'r') as f:
        for line in f.readlines():
            print(line, end='')
        print()

def search(eid):
    eid = str(eid)
    with open('/media/asadbek/D/maab/new/python-homeworks/lesson-6/homework/employees.txt', 'r') as f:
        for line in f.readlines():
            if line[:line.index(',')] == eid:
                return line
    return "not found"

# TODO update, delete function 
def update(eid, name, position, salary):
    with open('/media/asadbek/D/maab/new/python-homeworks/lesson-6/homework/employees.txt', 'r') as f:
        original = f.read()
# add_employee("Asadbek", "Backend developer", 50000)
# print(search(1001))
view()
update(1)