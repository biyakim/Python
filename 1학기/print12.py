# import random


# def rolling_dice(pip):
#     n = random.randint(1, pip)
#     print(pip, "면 주사위 굴린 결과 : ", n)


# rolling_dice(4)
# rolling_dice(6)
# rolling_dice(10)


# def rolling_dice(pip, repeat):
#     for r in range(1, repeat+1):
#         n = random.randint(1, pip)
#         print(pip, "면 주사위 굴린 결과 : ", r, ":", n)


# rolling_dice(4, 3)
# rolling_dice(6, 2)
# rolling_dice(10, 4)

# print()


# def func_sum(in_list):
#     sum = 0
#     li = in_list.split(" ")
#     for i in range(len(li)):
#         sum += int(li[i])
#     return sum


# in_list = input("데이타 입력 : ")
# print("합 : ", func_sum(in_list))

def p(*a):
    str = ""
    for i in a:
        str += (i+" ")
    print(str)


p("❤")
p("❤", "💥")
p("💤", "(*/ω＼*)", "💟", "😎")

print()


# def p(space, space_num, *args):
#     str = args[0]
#     for i in range(1, len(args)):
#         str = str+(space*space_num)+args[i]
#     print(str)


# p(",", 3, "😀", "😀")
# p("👣", 2, "🦿", "👀", "👁")
# p("_", 3, "👥", "👥", "👥", "👤")

# print()


# def star1(shape, *num):
#     for i in range(0, len(num)):
#         print(shape*num[i])


# star1("💭", 3)
# star1("❤", 1, 2, 3)

# print()

# def fn(a,b,c,*d):
#     print(a,b,c,d)

#     fn(c=3,b=2,a=1,4,5)
#     fn(1,2,c=3,4,5)
#     fn(4,5,a=1,b=2,c=3)
