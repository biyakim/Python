def star(mark,repeat,space,space_repeat,line):
    for i in range(1,line):
        str = (mark * repeat)
        str = str + (space * space_repeat) + (mark * repeat)
        print(str)

star("*",3,"_",2,4)