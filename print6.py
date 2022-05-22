from re import U


l = []
player = ["Messi", 10, True]
print(list("Happy"))
print(list((1125, 2463)))
print(list({"menu": "pizza", "price": 10000}))
print(list({"사과", "배"}))
nums = list(range(3))
print(nums)

print()

nums+[10, 11]
print(nums)
nums += [10, 11]
print(nums)
nums.append(20)
print(nums)
nums.append([30, 31])
print(nums)
nums.insert(2, 40)
print(nums)
nums.extend([50, 51])
print(nums)

print()

print(nums[7])
nums[7] = 60
print(nums)
del nums[2]
print(nums)
nums.remove(20)
print(nums)
nums.pop()
print(nums)
nums.pop(5)
print(nums)
nums.append(10)
print(nums)
nums.remove(10)
print(nums)
nums.clear()
print(nums)

print()

nums = list(range(3))
print(nums)
nums += [100, 10]
print(nums)
print(nums[3])
print(3 in nums)
print(10 in nums)

print()

print(len(nums))
nums.sort()
print(nums)
nums.reverse()
print(nums)

print()

t = ()
print(t)
xy = (2560, 1440)
print(xy)
color = 129, 247, 216
print(color)
print(xy+color)
print(xy*2)

print()

color = 129, 247, 216
print(color)
red, green, blue = color
print(red)
print(green)
print(blue)
x, y = 1920, 1080
print(x)
print(y)

print()

x = 2560
y = 1440
x, y = y, x
print(x)
print(y)
a = (123, "abc", True, 123)
print(a[1])
print(a[2:])
print(a[:2])
# a[1]=2
print(a.index("abc"))
print(a.count(123))
t = (1, 2, 3)
t += (4,)
print(t)

print()

d = {}
print(d)
urls = {"google": "google.com", 18: "unesco.org"}
print(urls)

print()

urls["x"] = 2560
print(urls)

print()

urls["x"] = 1920
print(urls)

print()

del urls["x"]
print(urls)
print(urls.pop(18))
urls.clear()
print(urls)

print()

urls = {"google": "google.com", 18: "unesco.org"}
print(urls["google"])
print(urls.get("google"))
print("google" in urls)
print("google.com" in urls)
print("google.com" in urls.values())

print()

print(len(urls))
print(urls.keys())
print(urls.values())
print(urls.items())

print()

game = {"LOL", "Overwatcg", "Tetris", 1942, 2048}
print(set("Funny"))
print(set([2048, "Tetris", "Cube"]))
print(set((2560, 1440)))
print({"google": "google.com", 18: "unesco.org"})
print(set(range(3)))

print()

print(game.add("Fifa"))
print(game.update(("NBA", "MLB")))

print()

print(game.remove("LOL"))

print()

s3 = {3, 6, 9, 12}
s4 = {4, 8, 12, 16}
print(s3 & s4)
print(s3.intersection(s4))

print()

print(s3 | s4)
print(s3.union(s4))

print()

print(s3 - s4)
print(s3.difference(s4))

print()

print(s3 ^ s4)
print(s3.symmetric_difference(s4))
