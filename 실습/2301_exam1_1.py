# 주민등록벊소 앞 6자리를 변수 id_number에 넣고, 출생년도 끝 두자리\n출생 월일\n 그 두개의 곱 출력
id_number = "020316"
print(id_number[0:2])
a = int(id_number[0:2])
print(id_number[2:])
b = int(id_number[2:])
c = a*b
print(c)
