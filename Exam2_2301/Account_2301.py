#2031 김비야
import random

money = 0
while(True):
    print("=================================================================")
    print("계좌 관리")
    print("=================================================================")
    print("1. 계좌생성      2. 입금 3. 출금 4. 잔액조회     0. 종료")
    print("=================================================================")
    menu = int(input("메뉴 선택 : "))
    if menu == 1:
        ran = random.randrange(0,999999999)
        print("계좌 번호",ran,"인 계좌가 생성되었습니다")
    if menu ==2:
        s = int(input("계좌번호 입력 : "))
        while(True):
            if s == ran:
                money_get = int(input("입금 금액 : "))
                print(ran,"에",money_get,"원이 입금되었습니다")
                money=money+money_get
                print("현재 잔액은 ",money,"원입니다")
                break
            elif s != ran:
                print("계좌번호",s,"가 존재하지 않습니다")
                s = int(input("계좌번호 입력 : "))

    if menu == 3 :
        s = int(input("계좌번호 입력 : "))
        while(True):
            if s == ran:
                money_out = int(input("출금 금액 : "))
                if(money_out < money):
                    print(ran,"에",money_out,"원이 출금되었습니다")
                    money=money-money_out
                    print("현재 잔액은",money,"원입니다.")
                    break
            elif s != ran:
                print("계좌번호",s,"가 존재하지 않습니다")
                s = int(input("계좌번호 입력 : "))
    if menu == 4 :
        print("=================================================================")
        print("계좌 번호        잔액")
        print("=================================================================")
        print(ran,"          ",money)
        print("=================================================================")

    if menu == 0:
        print("프로그램을 종료합니다")
        exit()
