# 2310 김비야
# 입력받아 거꾸로 출력하기
a=input("문자열 입력 : ")
reverse_name = ''

for c in a:
    reverse_name = c + reverse_name
print(reverse_name)