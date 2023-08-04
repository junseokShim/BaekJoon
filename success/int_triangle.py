N = int(input())

matrix = [[0]*(N+1)] + [[0] + [e for e in map(int, input().split(" "))] + [0]*(N-j-1) for j in range(N)]
dp = [[0]*(N+1) for _ in range(N+1)]

dp[1][1] = matrix[1][1]

for i in range(2, N+1):
    for j in range(1, i+1):
        dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + matrix[i][j]

print(max(dp[-1]))