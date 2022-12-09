class Person:
    count_class_var = 0

    def __init__(self,name,age,power):
        self.name = name
        self.age = age
        self.power = power
        self.increase_obj()

    def increase_obj(self):
            Person.count_class_var +=1

print("현재까지 생성된 인스턴스 객체의 갯수 : ",Person.count_class_var)
p1 = Person('이미림',20,9)
print("현재까지 생성된 인스턴스 객체의 갯수 : ",Person.count_class_var)
p1 = Person('김마이',17,4)
print("현재까지 생성된 인스턴스 객체의 갯수 : ",Person.count_class_var)