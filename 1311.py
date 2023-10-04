N = int(input())

# i번째 사람이 j번째 일을 할 때, 필요한 비용의 최소값 

graph = []
for _ in range(N):
    graph.append(list(map(int, input().split(" "))))


def dfs(i, visited):
    print(i, visited)
    # if visited == (1<<N)-1 :
    if i == N:
        return dp[visited]

    if dp[visited] == -1:
        dp[visited] = float("inf")
    else :
        return dp[visited]

    for j in range(0, N):
        if visited>>j & 0x1: continue
        dp[visited] = min(dp[visited], graph[i][j] + dfs(i+1, visited | (1 << j)))
        print(dp)
        
    return dp[visited]

dp = [-1]*(1<<(N))

print(dfs(0, 0))
