#2310 김비야
#소수와 개수를 출력하는 프로그램
def isPrimeNumber(num):
    print("1~N 까지의 소수와 그 갯수를 구하는 프로그램")
    print("N 입력 :",num)
    result=0
    print("소수 : ",end="")
    for i in range(1,num+1):
        count=0
        for k in range(1,i+1):
           if i%k==0:
            count+=1
        if count==2:
            result=result+1
            print(i," ",end="")
    print()
    print("1~23까지 소수의 갯수 :",result)     
       

isPrimeNumber(100)