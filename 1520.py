N, M = map(int, input().split())
matrix = [[0]*(M+1)]
for _ in range(N):
    matrix.append([0]+ list(map(int, input().split())))

cnt = 0
# dp에 대한 정의 필요 // dp를 통해 break 해야하나??
dp = [[0]*(M+1) for _ in range(N+1)]
visited = [[0]*(M+1) for _ in range(N+1)]
dirs = ((-1,0), (1,0), (0,-1), (0,1))

def dfs(x, y, visited):
    global dp, cnt
    if x == N and y == M:
        cnt += 1  
        return

    for d in dirs:
        nx, ny = x+d[0], y+d[1]
        if not 0 <= nx <= N:               continue
        if not 0 <= ny <= M:               continue 
        if matrix[x][y] <= matrix[nx][ny]: continue
        if visited[nx][ny] == 1:           continue

        visited[nx][ny] = 1
        dfs(nx, ny, visited)
        visited[nx][ny] = 0

    return


dfs(1,1,visited)
print(cnt)