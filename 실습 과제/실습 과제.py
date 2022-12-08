# 과제
# our_team = ["김비야", "김유진", "박선주", "백선미", "안소영",
#             "양혜원", "이혜령", "임재연", "최윤영", "최혜민", "하도연", "하진"]
# print(our_team[9])
# print(our_team[5:9])
# club = {"김비야": "영화감상반", "김유진": "코딩클리닉반", "박선주": "도서반", "백선미": "심리학연구반",
#         "안소영": "금융경제반", "양혜원": "피구반", "이혜령": "교지편집반", "임재연": "또래상담반",
#         "최윤영": "사진반", "최혜민": "코딩클리닉반", "하도연": "배드민턴반", "하진": "영화감상반"}
# print(club["안소영"])
# print(club[our_team[0]])

# print(331/17)
# x=37
# print(x**2)
# print(10**10)
# y=10e9
# print(y)
# a=123+456j
# print(a.conjugate())
# fun="funny day"
# fun.replace("day","Life")
# mon=[31,28,31,30,31,30,31,31,30,31,30,31]
# h=3
# m=15
# h,m=m,h


# x = int(input("숫자 : "))


# def is_prime_number(x):
#     # 2부터 (x - 1)까지의 모든 수를 확인하며
#     for i in range(2, x):
#         # x가 해당 수로 나누어떨어진다면
#         if x % i == 0:
#             return False  # 소수가 아님
#     return True  # 소수임


# if (is_prime_number(x)) == False:
#     print("소수가 아닙니다")
# elif (is_prime_number(x)) == True:
#     print("소수입니다")


# def star():
#         print('*'*5)
# star()
# star()
# star()

def a(p,m):
    print(p,"에 간다")
    return m+"은 산다"
    
a("우유","편의점")
result=a("홍차","대형마트")
if result !=True:
    a("홍차","편의점")
a("감자","시장")
