N, K = map(int, input().split())

C = []
for _ in range(N):
    C.append(int(input()))

C = sorted(C)

dp = [0]*(K+1)

dp[0] = 1 # 초기화 ...

for n, c in enumerate(C):
    for k in range(1, K+1):        
        if k>=c:
            dp[k] += dp[k-c]


print(dp[-1])