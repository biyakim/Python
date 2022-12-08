g = 1


def testScape(a):
    global g
    g = 2
    return g+a


print(testScape(1))
print(g)

print()


def swap(x, y):
    return y, x


print(swap(1, 2))
retValue = swap(1, 2)
print(retValue[0], retValue[1])

print()


def sum(*args):
    sum = 0
    for i in args:
        sum += i
    return sum


print("1+3 =", sum(1, 3))
print("1+3+5+7 =", sum(1, 3, 5, 7))

print()


def min(*numbers):
    min_value = numbers[0]
    for number in numbers:
        if min_value > number:
            min_value = number
    return min_value


print("1, 3", min(1, 3))

print()


def multi_num(multi, start, end):
    result = []
    for n in range(start, end):
        if n % multi == 0:
            result.append(n)
    return result


multi2 = multi_num(17, 1, 200)
print("multi_num(17,1,200) : ", multi2)
print()
multi3 = multi_num(3, 1, 100)
print("multi_num(3,1,100) : ", multi3)

print()


def min_max(*args):
    min = args[0]
    max = args[0]
    for arg in args:
        if min > arg:
            min = arg
        if max < arg:
            max = arg
        return min, max


print(min_max(52, -3, 23, 89, -21))
min_value, max_value = min_max(52, -3, 23, 89, -21)
print("최젓값 : ", min_value)
print("최곳값 : ", max_value)

print()


def div_name(name):
    surname = name[0]
    name1 = name[1:]
    return surname, name1


surname, name1 = div_name("김비야")
print("성 :", surname)
print("이름 :", name1)
