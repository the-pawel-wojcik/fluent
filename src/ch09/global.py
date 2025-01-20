from dis import dis

b = 6

def f1(a):
    print(a)
    print(b)
    b = 3


def f2(a):
    global b
    print(a)
    print(b)
    b = 9


print("Dis run on f1")
dis(f1)
print("Dis run on f2")
dis(f2)
