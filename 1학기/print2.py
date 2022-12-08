h = "  Happy Programming! "
print(len(h))
print(h.count("p"))
print(h.upper())
print(h.lower())
print(h.strip())
print(h.replace("Happy", "Funny"))
print(h.find("ap"))
print(h.rfind("a"))
print(h.find("zoo"))

print()

h = "  Hpaay Programming! "
print("a" in h)
print("amp" in h)
x = "01::23::ab::&&"
y = x.split("::")
print(y)
print(",".join(y))

print()

s = "name: {}, number:{},soccer:{}"
print(s.format("Ronaldo", 7, True))
print("name:{name},number:{num}".format(name="Jordan", num=23))

print()

print("{:d}".format(515))
print("{:5d}".format(515))
print("{:+5d}".format(515))
print("{:=+5d}".format(515))
print("{:05d}".format(515))
print("{:+05d}".format(515))

print()

print("{:f}".format(11.17))
print("{:12f}".format(11.17))
print("{:12.1f}".format(11.17))
print("{:=+6.1f}".format(11.17))

print()

a = 2
b = 3
s = '구구단 {0}*{1} = {2}'.format(a, b, a*b)
print(s)

print()

s1 = 'name:{0}'.format('BlockDMask')
print(s1)

print()

age = 55
s2 = 'age:{0}'.format(age)
print(s2)

print()

s3 = 'number:{num},gener:{gen}'.format(num=1234, gen='남')
print(s3)

print()

s4 = 'name:{},city:{}'.format('BlockDMask', 'Seoul')
print(s4)

print()

s5 = 'song1:{1},song2:{0}'.format('nunu nana', 'ice cream')
print(s5)

print()

s6 = 'test1:{0},test2:{1},test3{0}'.format('인덱스0', '인덱스1')
print(s6)

print()

s7 = 'Format example.{{}},{}'.format('test')
print(s7)

print()

s8 = 'This is value {{{}}}'.format(1212)
print(s8)

print()

s9 = 'this is {0:<10}|done{1:<5}|'.format('left', 'a')
print(s9)
s10 = 'this is {0:>10}|done{1:>5}|'.format('right', 'b')
print(s10)
s11 = 'this is {0:^10}|done{1:^5}|'.format('center', 'c')
print(s11)
s12 = 'this is {0:-<10}|done {1:o<5}|'.format('left', 'a')
print(s12)
s13 = 'this is {0:+>10}|done{1:0>5}|'.format('right', 'b')
print(s13)
s14 = 'this is {0:.^10}|done{1:@^5}|'.format('center', 'c')
print(s14)

print()

s15 = '정수 3자리:{0:03d},{1:03d}'.format(12345, 12)
print(s15)
s16 = '아래 2자리:{0:0.2f}, 아래 5자리:{1:0.5f}'.format(123.1234567, 3.14)
print(s16)

print()

a = 2
b = 1
#s='구구단 {0}*{1} = {2}'.format(a,b,a*b)
# print(s)
for a in range(2, 10):
    print('{0}단'.format(a))
    for b in range(1, 10):
        print('{0} * {1} = {2:2}'.format(a, b, a*b))
