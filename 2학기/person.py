class Person:
    def create_info(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print("----------------------------------------------------")
        print("이름 : ", self.name, "\n", "나이 : ", self.age)
        print("----------------------------------------------------")


p1 = Person()
p1.create_info('홍길동', 20)
p1.print_info()

p2 = Person()
p2.create_info('강감찬', 40)
p2.print_info()

p3 = Person()
p3.create_info('을지문덕', 30)
p3.print_info()
