## TASK 1: Zero check
def check(func):
    def fn(a, b):
        if b != 0:
            func(a, b)
        else:
            return "Denominator can't be zero"
    return fn

@check
def div(a, b):
    return a / b
print(div(2, 0))

## TASK 2: Employee manager
FILE = '/media/asadbek/D/maab/new/python-homeworks/lesson-6/homework/employees.txt'

def add_employee(name, position, salary):
    with open(FILE, 'a') as f:
        f.write('\n' + ', '.join(
                [str(id(name + position + str(salary))), name, position, str(salary)]
            )
        )
    print("------ EMPLOYEE ADDED ------\n")

def view():
    print("------ VIEW ALL ------")
    with open(FILE, 'r') as f:
        for line in f.readlines():
            print(line, end='')
    print("----------------------\n")


def search(eid):
    eid = str(eid)
    with open(FILE, 'r') as f:
        for line in f.readlines():
            if line[:line.index(',')] == eid:
                return line
    return "EMPLOYEE NOT FOUND"

def update(eid, name, position, salary):
    print("------ EMPLOYEE DATA UPDATED ------\n")
    text = ""
    with open(FILE, 'r') as f:
        for line in  f.readlines():
            if line.split(', ')[0] == str(eid):
                text += ', '.join([str(eid), name, position, str(salary)]) + "\n"
                continue
            text += line
    f = open(FILE, 'w')
    f.write(text)
    f.close()
    return True

def delete(eid):
    print("------ EMPLOYEE DELETED ------\n")
    text = ""
    with open(FILE, 'r') as f:
        for line in  f.readlines():
            if line.split(', ')[0] == str(eid):
                continue
            text += line
    f = open(FILE, 'w')
    f.write(text)
    f.close()
    return True

# add_employee("Asadbek", "Backend developer", 50000)

view()
update(140289708755344, "Asadbek", "Backend developer", 10000)
view()

delete(140289708755344)
view()

## TASK 3: word frequency
from collections import Counter
FILE = '/media/asadbek/D/maab/new/python-homeworks/lesson-6/homework/sample.txt'

def total():
    file = open(FILE, 'r')
    text = file.read().replace('.', '').replace(',', '.')
    c = Counter(text.lower().split())
    print("Total words:", len(c.keys()))
    text = file.read().replace('.', '').replace(',', '.')
    c = Counter(text.lower().split())
    for k, v in c.items():
        print(k, "-", v, 'times')

def wr():
    s = input("write in one line:")
    f = open(FILE, 'w')
    f.write(s)
    f.close()
    print("writted!")

def top():
    n = int(input("how many common words: "))
    file = open(FILE, 'r')
    text = file.read().replace('.', '').replace(',', '.')
    c = Counter(text.lower().split())
    for k, v in c.most_common(n):
        print(k, "-", v, 'times')


def hlp():
    print("""h - help
c - get most common words
w - write your own text
t - total
q - quit
    """)
running = True
hlp()
while running:
    command = input(">>$ ")
    if command == 'q':
        running = False
        break
    elif command == 'h':
        hlp()
    elif command == 't':
        total()
    elif command == 'c':
        top()
    elif command == 'w':
        wr()
    else:
        print('command not found')

print("bye")