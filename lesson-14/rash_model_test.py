import numpy as np
# Rash model test

questions = [0 for i in range(10)]
students = [{'name': 'user_1',
  'questions': [0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
  'result': None},
 {'name': 'user_2',
  'questions': [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  'result': None},
 {'name': 'user_3',
  'questions': [0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  'result': None},
 {'name': 'user_4',
  'questions': [0, 0, 1, 1, 1, 1, 0, 1, 1, 1],
  'result': None},
 {'name': 'user_5',
  'questions': [0, 1, 1, 1, 1, 1, 0, 0, 1, 1],
  'result': None},
 {'name': 'user_6',
  'questions': [0, 1, 1, 0, 0, 1, 0, 0, 0, 0],
  'result': None},
 {'name': 'user_7',
  'questions': [0, 0, 0, 1, 0, 1, 1, 0, 1, 1],
  'result': None},
 {'name': 'user_8',
  'questions': [0, 1, 1, 1, 1, 0, 0, 0, 0, 0],
  'result': None},
 {'name': 'user_9',
  'questions': [0, 0, 0, 1, 0, 1, 1, 0, 0, 1],
  'result': None},
 {'name': 'user_10',
  'questions': [0, 1, 0, 0, 1, 1, 0, 1, 1, 0],
  'result': None}
]
data = np.ndarray(shape=(10, 10), dtype=int)
ind = 0
for student in students:
    data[ind] = student['questions']
    ind += 1
def calc_q_score(q):
    return np.log2(1+len(students) / data.sum(axis=0)[q])

for i in range(10):
    score = calc_q_score(i)
    questions[i] = float(format(score, '.2f'))
print(questions)

def st_score(lst):
    s = 0
    index = 0
    for i in lst:
        if i:
            s += questions[index]
        index += 1
    return s

for i in range(10):
    students[i]['result'] = st_score(students[i]['questions'])
    print(students[i]['name'], "-", students[i]['result'])


# for i in range(10):
#     student = {
#         "name" : "user_" + str(i+1),
#         "questions" : [np.random.choice([1, 0]) for q in range(10)],
#         "result" : None
#     }
#     students.append(student)
# students