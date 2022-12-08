#2310 김비야
#점수대별로 해당 학생 수 만큼 별찍기
scores = list(map(int, input("점수 입력 : ").split()))
count = [0,0,0,0,0,0,]

for score in scores:
    if score >= 90:
        count[0] += 1
    elif score >=80:
        count[1]+=1
    elif score >=70:
        count[2]+=1
    elif score >=60:
        count[3]+=1
    elif score <60:
        count[4]+=1
print("90 이상 : ",count[0]*"*")
print("80정 대 : ",count[1]*"*")
print("70점 대 : ",count[2]*"*")
print("60점 대 : ",count[3]*"*")
print("60미만 대 : ",count[4]*"*")

print("최고점수 : ", max(scores))
print("최저점수 : ", min(scores))
        



