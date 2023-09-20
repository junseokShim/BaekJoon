N = int(input())
arr = []
for _ in range(N):
    arr.append(
        list(
            map(int, input().split())
            )
        )

dp = [[0 for _ in range(N)] for _ in range(N)]
dp[0][0] = 0

for l in range(N-1):
    for i in range(N-1-l):
        j = i + l + 1
        dp[i][j] = float("inf")
        for k in range(i, j):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j]+arr[i][0]*arr[k][1]*arr[j][1])

print(dp[0][-1])