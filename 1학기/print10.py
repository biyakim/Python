x = 3
while x < 6:
    print(x)
    x += 1

print()

# echo = input()
# while echo != "exit":
#     print(echo)
#     echo = input()

# print()

# echo = input()
# while True:
#     if echo == "exit":
#         break
#     print(echo)
#     echo = input()

print()

print(list(range(10)))
print(list(range(5, 10)))
print(list(range(10, 0, -1)))
print(list(range(10, 20, 2)))

print()

Lst = [1, 2, 3, 4, 5]
print(Lst)
Lst = [i**2 for i in Lst]
print(Lst)

print()

test = ("apple", "banana", "orange")
test_len = [len(i) for i in test]
print(test_len)

print()

d = {100: "apple", 200: "banana", 300: "orange"}
d_upper = [v.upper() for v in d.values()]
print(d_upper)

print()

lst = [10, 25, 30]
itel = filter(None, lst)
for item in lst:
    print("item:{0}".format(item))

print()


def getBiggerThan20(i):
    return i > 20


let = [10, 25, 30]
itel = filter(getBiggerThan20, lst)
for item in itel:
    print("item:{0}".format(item))
