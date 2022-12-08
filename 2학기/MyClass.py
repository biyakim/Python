class MyClass:
    a_var = 1000

    def a_method(self):
        self.a_var = 5000
        MyClass.a_var = 6000


print("[1]최초 클래스 변수의 초기값...>", MyClass.a_var)

MyClass.a_var = 3000
print("[2] 클래스 변수의 초기값을 3000으로 변경...>", MyClass.a_var)
#print("[2] 클래스 변수의 초기값을 3000으로 변경...>",a_var) #ERROR#

# 클래스내 메서드 호출을 통해서 변수값을 수정
m1 = MyClass()
m1.a_method()
print("[3] 클래스내 메서드 호출을 통해서 변수값을 수정...>", MyClass.a_var)

# 클래스 메서드 호출을 통해서 변수값 수정
# MyClass.a_method() #ERROR : self 주의
