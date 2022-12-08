#2310 김비야
#교집합 문자를 출력
def intersect(m1,m2):
    c=[]
    for i in m1:
        if i in m2:
            c.append(i)
    print(c)

intersect("HAM","SPAM")
