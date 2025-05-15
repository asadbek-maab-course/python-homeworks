s = input("s = ")
vowels = "aouie"
ans = ""
for i in s:
	if i in vowels:
		ans += "*"
	else:
		ans += i
print(ans)

