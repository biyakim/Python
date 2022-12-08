#2031_김비야
 
class Employee:
    
    def __init__(self,num,name,code,mon,y):
        self.type = num
        self.type = name
        self.type = code
        self.type = mon
        self.type = y

    def num(num,name,code,mon,y):
        if num[2:4] == "RM":
            print("Maneger******************************************************")
            if y == 0:
                print(num,"   ",name,"  ",code,"        ",mon)
            else:
                print(num,"   ",name,"  ",code,"        ",mon," ",y)

        elif num[2:4] == "TE":
            print("Templorary******************************************************")
            if y == 0:
                print(num,"   ",name,"  ",code,"        ",mon)
            else:
                print(num,"   ",name,"  ",code,"        ",mon," ",y)

        elif num[2:4] == "RS":
            print("SalesMan******************************************************")
            if y == 0:
                print(num,"   ",name,"  ",code,"        ",mon)
            else:
                print(num,"   ",name,"  ",code,"        ",mon," ",y)

Employee.num("MCRM1","강민준","B",30,0)
Employee.num("MCRS2","송서준","C",40,0)
Employee.num("MCTE3","고서윤","E",20,2)
Employee.num("MCRM4","민정우","B",30,0)
Employee.num("MCTE5","노수지","D",10,1)
Employee.num("MCTE6","이준영","E",20,3)
