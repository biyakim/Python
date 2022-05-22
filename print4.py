print("py""thon")
print("py"+"thon")
print("py"*3)

print()

strA = "python"
print(strA[0])

print()

strA = "python"
print(strA[0:1])
print(strA[1:3])
print(strA[:2])
print(strA[-2:])
print(strA[:])

print()

strB = "python is powerful"
print(strB[0])
print(strB[0:6])
print(strB[:6])

print()

strB = "python is powerful"
print(strB[-1])
print(strB[-2])
print(strB[-3:])
print(strB[-8:])

print()

strB = "python is powerful"
print(strB[7:18])
print(strB[:])
print(strB[::2])
print(strB[-11:-9])
print(strB[-18:-12])

print()

colors = ["red", "green", "blue"]
print(colors)
print(type(colors))

print()

print(colors)
colors.append("blue")
print(colors)

print()

print(colors)
colors.insert(1, "black")
print(colors)

print()

print(colors)
print(colors.index("red"))
colors += ["red"]
print(colors)
print(colors.index("red", 1))
colors += "red"
print(colors)

print()

print(colors)
print(colors.count("red"))
print(colors.pop())
print(colors.pop())
print(colors.pop(1))
print(colors)

print()

print(colors)
colors.remove("red")
print(colors)

print()

print(colors)
colors.extend(["blue", "yellow", "white"])
print(colors)

print()

print(colors)
colors.sort()
print(colors)
colors.reverse()
print(colors)

print()

a = {1, 2, 3, 4}
b = {3, 4, 4, 5}
print(a)
print(b)
print(type(a))
print(type(b))

print()

print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
