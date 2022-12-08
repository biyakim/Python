#파이썬 종합 문제 08/18

#001. Hello World 문자열 출력
print("Hello World")

#002. Mirim's Computer 문자열 출력
print("Mirim's Computer")

#003.
print('신씨가 소리질렀다. "도둑이야"')

#004.
print('"C:\Windows"')

#005.
print('안녕하세요.\n만나서\t\t반갑습니다.')

#006.
print("오늘은",'일요일')

#007. 
print('naver','kakao','samsung', sep=';')

#008.
print('naver/'+'kakao/'+'samsung')

#009.
print('first', end=''); print('second')

#010.
print(5/3)

#011. 삼성전자라는 변수로 50,000원을 바인딩해보세요. 
# 삼성전자 주식 10주를 보유하고 있을 때 총 평가금액 출력
삼성전자 = 50000
총평가금액 = 삼성전자 * 10
print(총평가금액)

#012.
시가총액 = 298
현재가 = 50000
PER = 15.79
print(f'시가총액 : {시가총액}조',type(시가총액))
print(f'현재가 : {현재가}원',type(현재가))
print(f'PER : {PER}', type(PER))

#013.
s = 'hello'
t = 'python'
print('hello{0} python'.format('!'))

#014.
print(2+2*3)

#015.
a = "132" #str
print(type(a))

#016.
num_str = "720"
print(int(num_str))

#017.
num = str(100)
print(num,type(num))

#018.
s = '15.79'
print(s,type(float(s)))

#019.
str = '2020'
year = int(str)
print(year-3)
print(year-2)
print(year-1)

#020. 에어컨 월 48584원, 무이자 36개월, 총금액 계산
money = 48584
sum = money * 36
print(sum)

#021.
letters = 'python'
print(letters[0],letters[2])

#022.
license_plate = "24가 2210"
print(license_plate[4:])

#023.
string = "홀짝홀짝홀짝"
print(string[1::2])

#024.
string = "python"
print(string[::-1])

#025.
phone_number = "010-1111-2222"
print(phone_number.replace('-',' '))

#026.
print(phone_number.replace('-',''))

#027.
url = "https://www.e-mirim.hs.kr"
url_split = url.split('.')
print(url_split[-1])

#028.
# lang = 'python‘
# lang[0] = 'P‘
# print(lang)

#029.
string = 'abcdfe2a354a32a'
string = string.replace('a','A')
print(string)

#030.
string = 'abcd'
string.replace('b', 'B')
print(string) #string 자체에 값이 바뀌지 않음