import sys
N = int(input())
W = [list(map(int, input().split(" "))) for _ in range(N)]


dp = [[0] * (1 << N - 1) for _ in range(N)]

def dfs(i, visited):
    if dp[i][visited] != 0: return dp[i][visited]               # dp 값이 0이 아니라면 이미 최소비용이 계산되었다는 의미임

    if visited == (1 << (N - 1)) - 1:                           # 모든 도시를 방문했을 경우,
        if W[i][0]:  return W[i][0]                             # 출발점으로 가는 경로가 있을 떄,
        else:  return float('inf')                              # 출발점으로 가는 경로가 없을 때,
            
    min_dist = float('inf')

    for j in range(1, N):                                       # 모든 도시를 탐방
        if not W[i][j]: continue                                # 가는 경로가 없다면 Skip
        if visited & (1 << j - 1): continue                     # 이미 방문한 도시라면 Skip

        # i 도시에서 j 도시로 갈 때,
        # j 도시를 방문한 것으로 표기 --> visited | (1<<(j-1))
        # dfs를 통해 j 도시에서 출발점으로 가는 최소 비용을 구함
        dist = W[i][j] + dfs(j, visited | (1 << (j - 1)))
        if min_dist > dist: min_dist = dist                     # 최소비용 갱신
        
    dp[i][visited] = min_dist                                   # 최소비용 설정
    
    return min_dist

print(dfs(0, 0))
