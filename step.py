N = int(input())
scores = [0] + [int(input()) for _ in range(N)]

dp = [0]*(N+1)

for i in range(1, N+1):
    dp[i] = max(dp[i-3]+scores[i-1]+scores[i], dp[i-2]+scores[i])

print(dp[-1])