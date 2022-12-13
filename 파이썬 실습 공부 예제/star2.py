def star(pip,*args):
    for arg in args:
        print(pip*arg)

star("*",3)
star("&",1,2,3)