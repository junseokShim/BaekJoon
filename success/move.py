N, M = map(int, input().split(" "))

matrix = [[0 for _ in range(M+1)]] + [[0] + [e for e in map(int, input().split(" "))] for _ in range(N)]

dp = [[0 for _ in range(M+1)] for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, M+1):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + matrix[i][j]
        
        
print(dp[N][M])