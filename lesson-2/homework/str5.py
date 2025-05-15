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
