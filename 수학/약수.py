n = int(input())
divisors = list(map(int, input().split()))

if n==1: print(divisors[0]**2)
else:      
    divisors = sorted(divisors)
    print(divisors[0]*divisors[-1])