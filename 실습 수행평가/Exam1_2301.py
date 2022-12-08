# 2301 김비야

# 문제 1
# a = int(input("정수1 입력 : "))
# b = int(input("정수2 입력 : "))

# if a > b:
#     a, b = b, a
# print()
# for i in range(a, b+1):
#     print(i, "단")
#     for j in range(1, 10):
#         print(i, "*", j, "=", i*j)
#     print()

# print()

# 문제 2
# sum = 0
# d = []
# for i in range(5):
#     a = int(input(str(i+1)+" 입력 : "))
#     d.append(a)
#     sum += a

# print("입력된 점수 : ", d[0], d[1], d[2], d[3], d[4])
# print("합계 :", sum)
# avg = sum/5
# print("평균 : %.2f " % avg)
# if avg >= 60:
#     print("%.2f" % avg, "점으로 합격입니다.")
# else:
#     print("%.2f" % avg, "점으로 불합격입니다.")
# print()

# 문제 3
price={"메로나":[1000,20],"비비빅":[700,3],"바밤바":[850,100]}

# 문제3-1
print(" 상품명", "    가격", "    수량")
for key in price.keys():
    print(key,"   ",price[key][0],"   ",price[key][1])

# 문제3-2
a1 = input("상품명 입력 : ")
b1 = int(input("가격 입력 : "))
c1 = int(input("수량 입력 :"))
price[a1] = [b1,c1]
for key in price.keys():
    print(key,"   ",price[key][0],"   ",price[key][1])

# 문제3-3
name = str(input("상품명 입력 : "))
print("1. 가격  수정")
print("2. 수량  수정")
m = int(input("메뉴 입력 : "))
if m == 1:
    p = int(input("가격 입력 : "))
    price[name][0] = p
    for key in price.keys():
        print(key,"   ",price[key][0],"   ",price[key][1])
if m == 2:
    l = int(input("수량 입력 : "))
    price[name][1] = l
    for key in price.keys():
        print(key,"   ",price[key][0],"   ",price[key][1])



print()

# 문제3-4
name1 = input("상품명 입력 : ")
del price[name1]
for key in price.keys():
    print(key,"   ",price[key][0],"   ",price[key][1])
# 문제3-5
print("1. 신규 상품 등록")
print("2. 상품 수정")
print("3. 상품 삭제")
print("4. 상품 조회")
print("0. 종료")
me = int(input("메뉴 입력 : "))
for i in range(5):
    if me == 0:
        break
    print("프로그램이 종료됩니다")
print()
