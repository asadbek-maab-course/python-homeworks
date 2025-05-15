s = input("s = ")
for i in "0987654321":
	if i in s:
		print("s contains digit")
		break
else:
	print("s not contains digit")
