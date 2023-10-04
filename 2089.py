import sys
N = int(input())
W = [list(map(int, input().split(" "))) for _ in range(N)]


dp = [[0] * (1 << N - 1) for _ in range(N)]


def dfs(start, visited):
    if visited == (1<<N)-1:
        return W[start][0]
        
    if dp[start][visited] != 0:
        return dp[start]

print(dfs(0, 0))
