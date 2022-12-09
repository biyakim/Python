class MyClass:
    a_var = 1000

    def a_method(self):
        self.a_var = 5000
        MyClass.a_var = 6000
        return self.a_var


m1 = MyClass()
print(m1.a_method())
