# 1.py
fl = float(input())
print(f"{fl:.2f}")

# 2.py
n1, n2, n3 = map(int, input().split())
print(max([n1, n2, n3]), min([n1, n2, n3]))


# 3.py
n = float(input("Uzunlikni km da kiriting: "))
m = n * 1000
sm = m * 100
print(f"{n} km = {m} metr {sm} santimetr")


# 4.py
a, b = map(int, input("a va b ni kiriting: ").split())
c = a // b
d = a % b
print(f"{a}//{b} = {c}")
print(f"{a} mod {b} = {d}")


# 5.py
c = int(input("haroratni C da kiriting: "))
print(f"Farangeyda {c}C = {c+32}")


# 6.py
n = int(input("n = "))

print(f"n ning oxiri: {n%10}")


# 7.py
n = int(input("n = "))

if n % 2:
	print("Toq")
else:
	print("Juft")


# str10.py
s = input("s = ")
print("len =", len(s.split()))


# str11.py
s = input("s = ")
for i in "0987654321":
	if i in s:
		print("s contains digit")
		break
else:
	print("s not contains digit")


# str12.py
s = input("write list of word with space: ")
print('-'.join(s.split()))


# str13.py
s = input("s = ")
print(s.replace(' ', ''))


# str14.py
a = input("s1 = ")
b = input("s2 = ")
if a == b:
	print("They are equal")
else:
	print("They are not equal")



# str15.py
s = input("s = ")
ans = ""
for i in s.split():
	ans += i[0]
print(ans)


# str16.py
s = input("s = ")
c = input("char = ")
print(s.replace(c, ''))


# str17.py
s = input("s = ")
vowels = "aouie"
ans = ""
for i in s:
	if i in vowels:
		ans += "*"
	else:
		ans += i
print(ans)



# str18.py
s = input("s = ")
st = input("start with: ")
e = input("end with: ")
print(s, ("" if s.startswith(st) else " not") + "start with", st)
print(s, ("" if s.endswith(e) else " not") + "end with", e)


# str1.py
name = input("ismingiz: ")
y = int(input("tug'ilgan yilingiz: "))
print(f"{name} {2025-y} yoshda")


# str2.py
txt = "LMaasleitbtui"
print(txt[::2])


# str3.py
s = input("satr kiriting: ")
print(f"uzunlik: {len(s)}")
print(s.upper())
print(s.lower())


# str4.py
s = input("satr kiriting: ")
if s == s[::-1]:
	print("palindrom")
else:
	print("palindrom emas")


# str5.py
s = input("s = ")
vowels = "aoeiu"
consonants = "bcdfghjklmnpqrstvwxyz"
cnt = 0
cntc = 0
for i in s:
	if i in vowels:
		cnt += 1
	elif i in consonants:
		cntc += 1
print("unli harflar:", cnt)
print("undosh harflar:", cntc)


# str6.py
s1 = input("s1 = ")
s2 = input("s2 = ")
if s1 in s2:
	print("s2 ichida s1 bor")
elif s2 in s1:
	print("s1 ichida s2 bor")
else:
	print("bir birini ichida yo'q")



# str7.py
s = input("Sentence: ")
repl = input("replace: ")
w = input("with: ")
print(s.replace(repl, w))


# str8.py
s = input("s = ")
print(f"first: {s[0]}, last: {s[-1]}")


# str9.py
s = input("s = ")
print(s[::-1])



