p = "881120-1068234"
print("연월일 : ", p[0:6])
print("숫자 : ", p[7:])

print()

print("성별 : ", p[7])

print()

l = [1, 3, 5, 4, 2]
print("원본 : ", l)
l.sort()
l.reverse()
print("결과 : ", l)

print()

l2 = ['life', 'is', 'too', 'short']
print(" ".join(l2))

print()

t = (1, 2, 3)
t += (4,)
print(t)

print()

a = {'A': 90, 'B': 80, 'C': 70}
print("원본 : ", a)
b = a.pop("B")
print("'B' 추출 후 딕셔너리 : ", a)
print("B 추출 값 : ", b)

print()

a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
print("원본 : ", a)
b = set(a)
print("중복제거 후 : ", list(b))

print()
