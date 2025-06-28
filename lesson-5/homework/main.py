## TASK 1
def convert_cel_to_far(c):
    return c * 9/5 + 32

def convert_far_to_cel(f):
    return (f - 32) * 5/9

f = int(input("Enter a temperature in degrees F: "))
print(f"{f} degress F = {convert_far_to_cel(f): .2f} degrees C")
c = int(input("Enter a temperature in degrees C: "))
print(f"{c} degress C = {convert_cel_to_far(f): .2f} degrees F")

## TASK 2
def invest(amount, rate, years):
    for i in range(1, years+1):
        amount = float(format(amount*(1+rate), '.2f'))
        print(f'year {i}: $', amount)

invest(100, .05, 4)

## TASK 3
n = int(input("n = "))
a = (i for i in range(1, n+1) if n % i == 0)
for i in a:
    print(f"{i} is a factor of {n}")

## TASK 4
universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]
def enrollment_stats(data):
    return [[i[1] for i in data], [i[2] for i in data]]
def mean(a):
    return float(format(sum(a) / len(a), '.2f'))

def median(a):
    a.sort()
    l = len(a)
    return a[l//2]
x = 0
print("******************************")
for i in enrollment_stats(universities):
    if x == 0:
        print(f"Total students: {sum(i):,}")
        x = 1
    else:
        print(f"Total tuition: ${sum(i):,}")
x = 0
print()
for i in enrollment_stats(universities):
    if x == 0:
        print(f"Student mean: {mean(i):,}")
        print(f"Student median: {median(i):,}")
        x = 1
    else:
        print()
        print(f"Tuition mean: {mean(i):,}")
        print(f"Tuition median: {median(i):,}")
print("******************************")

## TASK 5
def is_prime(n):
    if n == 2: return True
    elif n < 2 or n % 2 == 0: return False
    else:
        i = 3
        while i*i <= n:
            if n % i == 0:
                return False
            i += 2
        return True

print(is_prime(19))