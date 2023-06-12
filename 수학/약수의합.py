n = int(input())
numbers = [int(input()) for _ in range(n)]

MAX = 1000000
dp = [0]+[1]*(MAX)
s = [0]*(MAX+1)

for i in range(2, MAX+1):
    j = 1
    while i*j <= MAX:
        dp[i*j] += i
        j+=1


for i in range(1, MAX+1):
    s[i] = s[i-1] + dp[i]

for number in numbers:
    print(s[number])