def prime(start,end):
    a= []
    for i in range(start,end):
        flag = True
        for j in range(2,i):
            if i % j == 0:
                flag =  False
                break
        if flag:
            a.append(i)
    return a

print(prime(1,50))