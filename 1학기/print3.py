import keyword
num = 50
s = 'my age %d' % num
print(s)

print()

names = ['Kim', 'park', 'lee']
for name in names:
    print('my name is %s' % name)

print()

money = 10000
s2 = 'give me %d won' % money
print(s2)

print()

d = 3.141592
print('value %f' % d)

print()

s1 = 'my name is %s, age: %d' % ('mirim', 100)
print(s1)

print()

age = 78
money = 20000
name = 'Jang'
weight = 63.12
etc = 'abcde'
s2 = 'my name is %s, age:%d, weight:%f, money:%d, etc:%s' % (
    name, age, weight, money, etc)
print(s2)

print()

month = 1
while month <= 12:
    print(f'2020년{month}월')
    month = month+1

print()

s = 'coffee'
n = 5
result1 = f'저는{s}를 좋아합니다.하루{n}잔 마셔요'
print(result1)

print()

# f-string 왼쪽 정렬
s1 = 'left'
result1 = f'|{s1:<10}|'
print(result1)
# f-string 가운데 정렬
s2 = 'mid'
result2 = f'|{s2:^10}|'
print(result2)
# f-string 오른쪽 정렬
s3 = 'right'
result3 = f'|{s3:>10}|'
print(result3)

print()

num = 10
result = f'my age {{{num}}},{{num}}'
print(result)

print()

d = {'name': 'Mirim', 'gender': 'female', 'age': 18}
result = f'my name {d["name"]}, gender{d["gender"]}, age{d["age"]}'
print(result)

print()

n = [100, 200, 300]
print(f'list:{n[0]},{n[1]},{n[2]}')

for v in n:
    print(f'list with for:{v}')

print()

strB = "파이썬 연습"
print(len(strB))

print()

strA = "Hello python"
x = 5
y = 3.14
print(type(strA))
print(type(x))
print(type(y))

print()

print(keyword.kwlist)
