from random import choice, randint
# 1.py
list1 = [1, 2, 3, 4, 5]
list2 = [2, 3, 3, 6, 6, 7]
commons = set(list1) & set(list2)
uncoms = []
for i in list2 + list1:
    if not i in commons:
        uncoms.append(i)
if uncoms == []:
    print("hamma elementlar umumiy")
else:
    print(uncoms)



# 2.py
n = int(input())
for i in range(1, n):
    print(i*i)

# 3.py
txt = input("txt: ")
cnt = 0
undered = []
for i in range(len(txt)):
    if cnt >= 2:
        if not txt[i] in undered and not txt[i] in 'aioeu' and i < len(txt)-1:
            print(txt[i], "_", sep="", end="")
            cnt = 0
            undered += [txt[i]]
            continue
    print(txt[i], end='')
    cnt += 1


# 4.py
num = randint(1, 100)
attemps = 0
again = True
while again:
    if attemps >= 10:
        print("Too many attempts")
        break
    guess = int(input("guess: "))
    if guess > num:
        print('Too high!')
    elif guess < num:
        print('Too low!')
    else:
        print("You guessed it right!")
        again = input("You lost. Want to play again?")
        again = (again in ["Y", "YES", "yes", "y", "ok"])
        attemps = 0
        num = randint(1, 100)
        continue
    attemps += 1
print("Good bye")


# 5.py
password = input("Pasword: ")
def check(password):
    if len(password) < 8:
        return "Too short"
    for i in set(password):
        if i == i.upper() and not i.isdigit():
            break
    else:
        return "Password must contain an uppercase letter"
    return "Password is strong"
print(check(password))

# 6.py
def p(n):
    if n == 2: return True
    elif n < 2 or n % 2 == 0: return False
    else:
        i = 3
        while i*i <= n:
            if n % i == 0:
                return False
            i += 2
        return True

for i in range(1, 101):
    if p(i):
        print(i, end=" ")

# bonus.py


print("Rock(r), Paper(p), Scissors(s)")
c_user = c_cpu = 0
wins = {
    'r' : 's',
    's' : 'p',
    'p' : 'r'
}
characters = {
    'r' : 'rock',
    'p' : 'paper',
    's' : 'scissors'
}
while True:
    cpu = choice(['r', 'p', 's'])
    user = input("choice r/p/s : ")
    print("---------------")
    print("You: {}  ||  Cpu : {}".format(characters[user], characters[cpu]))
    if user != cpu:
        if wins[user] == cpu:
            print("You win")
            c_user += 1
        else:
            print("You lose")
            c_cpu += 1
    else:
        print("Draw")
    print(f"Scores: you: {c_user} || cpu : {c_cpu}")
    if max(c_cpu, c_user) >= 5:
        if c_cpu >= 5:
            print("Cpu is winner")
        else:
            print("Ypu winner")
        break

