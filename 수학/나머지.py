a, b, c = map(int, input().split())

def method_1(a,b,c):
    return (a+b)%c

def method_2(a,b,c):
    return ((a%c)+(b%c))%c

def method_3(a,b,c):
    return (a*b)%c

def method_4(a,b,c):
    return ((a%c)*(b%c))%c


methods = [method_1(a,b,c), method_2(a,b,c), method_3(a,b,c), method_4(a,b,c)]

for method in methods:
    print(method)