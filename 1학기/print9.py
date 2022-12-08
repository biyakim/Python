print(bool(True))
print(bool(False))
print(bool(0))
print(bool(3))
print(bool(""))
print(bool("test"))
print(bool([]))
print(bool([1, 2, 3]))

print()

# a = int(input("입력 : "))
# if a % 2 == 0 and a < 0:
#     print("minus")
#     print("even")
# elif a % 2 == 1 and a > 0:
#     print("plus")
#     print("odd")
# elif a % 2 == 0 and a > 0:
#     print("plus")
#     print("even")
# elif a % 2 == 1 and a < 0:
#     print("minus")
#     print("odd")

print()

table = [["월", "화", "수"], [100, 200, 300]]
for row in table:
    for col in row:
        print(str(col)+" ")
    print()

print()

Lst = ["apple", 100, 3.14]
for i in range(3):
    print(Lst[i], type(Lst[i]))

print()

d = {"apple": 100, "orange": 200, "banana": 300}
for k, v in d.items():
    print(k, v)

print()

a = [(1, 2), (3, 4), (5, 6)]
for (first, last) in a:
    print(first+last)

print()

for i in range(1, 11):
    for j in range(i):
        print("*", end="")
    print()

print()

for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    print("*"*i)

print()

for i in range(1, 11):
    print("*"*i)

print()

for i in range(1, 9+1):
    print("2 x {} = {}".format(i, 2*i))
for i in range(1, 9+1):
    print("3 x {} = {}".format(i, 3*i))
for i in range(1, 9+1):
    print("4 x {} = {}".format(i, 4*i))
for i in range(1, 9+1):
    print("5 x {} = {}".format(i, 5*i))

print()

for i in range(1, 6):
    print(" "*(5-i), end=" ")
    print("*"*(2*i-1))

print()

table = [["월", "화", "수"], [100, 200, 300]]
for row in table:
    for col in row:
        print(str(col)+" ")
    print()

print()

for i in range(1, 9+1):
    if i == 7:
        break
    print("2 x {} = {}".format(i, 2*i))

print()

for i in range(1, 9+1):
    if i % 2 == 0:
        continue
    print("2 x {} = {}".format(i, 2*i))

print()

Lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for item in Lst:
    if item > 5:
        break
    print("item:{0}".format(item))

print()

array = []
for i in range(1, 10, 2):
    array.append(i*i)
print(array)

array = [i*i for i in range(1, 10, 2)]
print(array)

array = [i*i for i in range(1, 10, 2) if i*i > 30]
print(array)
