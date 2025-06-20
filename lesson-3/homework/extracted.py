# task-1
l = [1, 2, 3, 2, 1, 2, 1, 1, 1]
element = 1
print(l.count(element))

# task-2
print(sum(l))

# task-3
print(f"max: {max(l)}")
print(f"min: {min(l)}")

# task-4
element = 5
if element in l:
    print(f"{element} listda bor")
else:
    print(f"{element} listda yo'q")

# task-5
l2 = []
if l2 == []:
    print("list bo'sh")
else:
    print("birinchi element: ", l2[0])

# task-6
if l == []:
    print("list bo'sh")
else:
    print("oxirgi element ", l[-1])

# task-7
listslice = l[:3]
print(listslice)

# task-8
reverse_list = reversed(l)
print(list(reverse_list))

# task-9
sortlist = sorted(l)
print(sortlist)

# task-10
dl = []
for i in l:
    if i not in dl:
        dl.append(i)
print(dl)

# task-11
index = 2
element = 4
l.insert(index, element)
print(l)

# task-12
element = 3
print(l.index(element))

# task-13
print(l == [])

# task-14
cnt = 0
for i in l:
    cnt += (i % 2 == 0)
print(cnt)

# task-15
cnt = 0
for i in l:
    cnt +=  (i % 2)
print(cnt)

# task-16
new_list = [5, 6, 7]
comb_list = l + new_list
print(comb_list)

# task-17
sub = [4, 3]
leng = len(sub)
for i in range(len(l) - leng + 1):
    if l[i:i+leng] == sub:
        print("index: ", i)
        break
else:
    print("sub list yo'q")

# task-18
element = 4
repl = 5
if element in l:
    l[l.index(element)] = 5
    print(l)
else:
    print(f"{element} listda yo'q")


# task-19
nums = set(l)
print(l)
print("second largest:", sorted(nums, reverse = 1)[1])

# task-20
nums = set(l)
print(l)
print("second smallest:", sorted(nums)[1])

# task-21
new_list = [i for i in l if i % 2 == 0]
print(new_list)

# task-22
new_list = [i for i in l if i % 2 == 1]
print(new_list)

# task-23
print("elementlar soni:", len(set(l)))

# task-24
new_list = l.copy()
print("l copy:", new_list)

# task-25
leng = len(l)
if leng % 2:
    print("middle:", l[leng // 2])
else:
    print("middles", l[leng//2:leng//2+2])


# task-26
sublist = l[5:9]
print("max:", max(sublist))

# task-27
sublist = l[5:9]
print("min:", min(sublist))

# task-28
index = 6
if len(l) > index:
    del l[index]
    print(f"{index} indexdagi o'chirildi")
else:
    print(f"{index} index mavjud emas")
print(l)

# task-29
print(l == list(sorted('l')))

# task-30
print("")

