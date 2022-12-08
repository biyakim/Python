from hashlib import sha3_224
from re import T


t = (1, 2, 3)
print(type(t))

print()


def colc(a, b):
    return a+b, a*b


x, y = colc(5, 4)
print(x, y)

print()

print("id : %s, name : %s" % ("Kim", "김유신"))

print()

args = (3, 4)
print(colc(*args))

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

print()

print(a | b)
print(a & b)
print(a - b)

print()

a = set((1, 2, 3))
print(a)
print(type(a))

print()

b = list(a)
print(b)
print(type(b))

print()

c = tuple(b)
print(c)
print(type(c))

print()

d = dict(a=1, b=2, c=3)
print(d)
print(type(d))

print()

colors = {"apple": "red", "banana": "yellow"}
print(colors)

print()

colors["cherry"] = "red"
print(colors)

print()

for item in colors.items():
    print(item)

print()

for k, v in colors.items():
    print(k, v)

print()

print(colors)
del colors["cherry"]
print(colors)
colors.clear()
print(colors)

print()

device = {"아이폰": 5, "아이패드": 10, "윈도우타블렛": 20}
device["아이맥"] = 15
device["아이폰"] = 6
print(device)
del device["아이폰"]
print(device)

print()

phone = {"Kim": "1111", "Lee": "2222", "park": "3333"}
print(phone.keys())
print(phone.values())

print()

print("park" in phone)
print("moon" in phone)

print()

p = phone
print(p)

print()

d = {"a": 100, "b": 200, "c": 300}

for key in d.keys():
    print(key)

for value in d.values():
    print(value)

print()

isRight = False
print(type(isRight))
print(1 < 2)
print(1 != 2)
print(1 == 2)
print(True and True and False)
print(True or False or False)

print()

print(bool(0))
print(bool(-1))
print(bool("test"))
print(bool(None))
print(bool(""))
print(bool(" "))
print(bool(''))
print(bool(' '))

# mutable 종류: list,set,dictionary
# immutable 종류 : int,float,str,bool,tuple

print()

print("immutable 객체")
a = 99
b = 99
c = 99
d = 99
e = 99
print(hex(id(a)))
print(hex(id(b)))
print(hex(id(c)))
print(hex(id(d)))
print(hex(id(e)))

print()

print("mutable 객체")
arr1 = [1, 2, 3]
arr2 = [1, 2, 3]
arr3 = [1, 2, 3]
arr4 = [1, 2, 3]
print(hex(id(arr1)))
print(hex(id(arr2)))
print(hex(id(arr3)))
print(hex(id(arr4)))

print()

# immutable 객체
print("="*50)
print("immutable 객체 예제")
print("="*50)
print("1. int 값이 변경되면?")
num1 = 99
num2 = 99
num3 = 99
num4 = 99
print(f"num1 값: {num1} \t주소 : {hex(id(num1))}")
print(f"num2 값: {num2} \t주소 : {hex(id(num2))}")
print(f"num3 값: {num3} \t주소 : {hex(id(num3))}")
print(f"num4 값: {num4} \t주소 : {hex(id(num4))}")
num1 += 1  # num1 값 증가
num3 += 1  # num3 값 증가
num4 += 10  # num4 값 증가
print(f"num1 값: {num1} \t주소 : {hex(id(num1))}")
print(f"num2 값: {num2} \t주소 : {hex(id(num2))}")
print(f"num3 값: {num3} \t주소 : {hex(id(num3))}")
print(f"num4 값: {num4} \t주소 : {hex(id(num4))}")

print()

print("\n2.str값이 변경되면?")
s1 = "BlockDMask"
s2 = "BlockDMask"
s3 = "BlockDMask"
s4 = "BlockDMask"
print(f"s1 값: {s1} \t주소 : {hex(id(s1))}")
print(f"s2 값: {s2} \t주소 : {hex(id(s2))}")
print(f"s3 값: {s3} \t주소 : {hex(id(s3))}")
print(f"s4 값: {s4} \t주소 : {hex(id(s4))}")
s1 = s1.replace('D', 'ZZZZ')  # replace 로 값을 변경하고, 새로운 문자열을 s1로 대하게 됨
s2 = "BlockZZMask"  # replace로 변경한 문자열과 동일한 문자열로 변경함
s4 = s3.upper()  # s4를 대문자로 변경
print(f"s1 값: {s1} \t주소 : {hex(id(s1))}")
print(f"s2 값: {s2} \t주소 : {hex(id(s2))}")
print(f"s3 값: {s3} \t주소 : {hex(id(s3))}")
print(f"s4 값: {s4} \t주소 : {hex(id(s4))}")

print()

# 리스트 내부의 mutable 요소
print("-"*50)
print("리스트 내부의 mutable 요소들")
arr1 = [55, 66, [11, 22], 'a', 'b']
arr2 = [55, 66, [11, 22], 'a', 'b']
print(f"arr1[0] :{arr1[0]}\t주소: {hex(id(arr1[0]))}")
print(f"arr2[0] :{arr2[0]}\t주소: {hex(id(arr2[0]))}")
print(f"arr1[1] :{arr1[1]}\t주소: {hex(id(arr1[1]))}")
print(f"arr2[1] :{arr2[1]}\t주소: {hex(id(arr2[1]))}")
print(f"arr1[3] :{arr1[3]}\t주소: {hex(id(arr1[3]))}")
print(f"arr2[3] :{arr2[3]}\t주소: {hex(id(arr2[3]))}")
print(f"arr1[4] :{arr1[4]}\t주소: {hex(id(arr1[4]))}")
print(f"arr2[4] :{arr2[4]}\t주소: {hex(id(arr2[4]))}")

print()


# mutable 객체
print("="*50)
print("mutable 객체 예제.")
print("="*50)
print("1.list 값이 변경되면?")
arr1 = ['a', 'b', 77]
arr2 = ['a', 'b', 77]
arr3 = ['a', 'b', 77]
print(f"arr1 값: {arr1} \t주소 : {hex(id(arr1))}")
print(f"arr2 값: {arr2} \t주소 : {hex(id(arr2))}")
print(f"arr3 값: {arr3} \t주소 : {hex(id(arr3))}")
arr1.append(10)
arr2.append(10)
print(f"arr1 값: {arr1} \t주소 : {hex(id(arr1))}")
print(f"arr2 값: {arr2} \t주소 : {hex(id(arr2))}")
print(f"arr3 값: {arr3} \t주소 : {hex(id(arr3))}")

print()

print("\n2.dictionary 값이 변경되면?")
d1 = {'a': 11, 'b': 22, 'c': 33}
d2 = {'a': 11, 'b': 22, 'c': 33}
d3 = {'a': 11, 'b': 22, 'c': 33}
print(f"d1 값: {d1} \t주소 : {hex(id(d1))}")
print(f"d2 값: {d2} \t주소 : {hex(id(d2))}")
print(f"d3 값: {d3} \t주소 : {hex(id(d3))}")
d1['a'] = 99
d2['d'] = 44
print(f"d1 값: {d1} \t주소 : {hex(id(d1))}")
print(f"d2 값: {d2} \t주소 : {hex(id(d2))}")
print(f"d3 값: {d3} \t주소 : {hex(id(d3))}")

print()

student_grade = 2
student_class = 3
student_number = 1
student_name = "김비야"
student_height = 154.9

print()

print(type(student_grade))
print(type(student_class))
print(type(student_number))
print(type(student_name))
print(type(student_height))

print()

print("="*50)
print("mutable 객체 요소로 존재하는 imutable,mutable")
print("="*50)
arr1 = [55, 66, [11, 22], 'a', 'b']
arr2 = [55, 66, [11, 22], 'a', 'b']
# 리스트(imutable)객체의 주소
print(f"arr1: {arr1} \t주소 :{hex(id(arr1))}")
print(f"arr2: {arr2} \t주소 :{hex(id(arr2))}")

print()

print("-"*50)
print('리스트 내부의 mutable 요소들')
print(f"arr1[2] : {arr1[2]} \t주소: {hex(id(arr1[2]))}")
print(f"arr2[2] : {arr2[2]} \t주소: {hex(id(arr2[2]))}")
