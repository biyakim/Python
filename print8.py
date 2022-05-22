print(bin(0b1010))
print(bin(0b1010 & 0b0110))
print(bin(0b1010 | 0b0110))
print(bin(0b1010 ^ 0b0110))
print(bin(~0b1010))
print(~0b1010)

print()

print((0b1010))
print((0b1010 & 0b0110))
print((0b1010 | 0b0110))
print((0b1010 ^ 0b0110))

print()

print(bin(0b1010 << 2))
print((0b1010 << 2))
print(bin(0b1010 >> 2))
print((0b1010 >> 2))

print()

a = 3
if a > 5:
    print("test입니다")
    print("a=10입니다")
else:
    print("else문입니다")

print()

# x = int(input())
# print(x)
# print(type(x))

print()

# x = int(input("숫자입력 : "))
# if x % 2 == 0:
#     print("짝수")
# else:
#     print("홀수")

# print()

# password = input("암호 입력 : ")

# if password == "암호":
#     print("암호이다")
# else:
#     print("암호가 아니다")

print()

money = 1
if money:
    print("택시를")
print("타고")
# print("가자")

print()

money = 2000
if money >= 3000:
    print("택시를 타고 가라")
else:
    print("걸어 가라")

print()

money = 2000
card = 1
if money >= 3000 or card:
    print("택시를 타고 가라")
else:
    print("걸어 가라")

print()

pocket = ['paper', 'cellphone', 'money', 'card']
if 'money' in pocket:
    print("택시를 타고 가라")
else:
    print("걸어 가라")

print()

if 'money' in pocket:
    pass
else:
    print("카드를 꺼내라")
print("수행 완료")

print()

if 'money' not in pocket:
    print("카드를 꺼내라")
print("수행 완료")

print()

if 'money' in pocket:
    print("택시를 타라")
elif 'card' in pocket:
    print("택시를 타라")
else:
    print("걸어 가라")

print()

saying = "Life is too short, you need python"

if "wife" in saying:
    print("wife")
elif "python" in saying and "you" not in saying:
    print("python")
elif "shirt" not in saying:
    print("shirt")
elif "need" in saying:
    print("need")
else:
    print("none")
