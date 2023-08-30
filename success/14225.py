N = int(input())
matrix = list(map(int, input().split(" ")))

cnt = 0
vals = [0]*2000000
visited = [0 for _ in range(N+1)]

def dfs(idx, arr):
    global cnt
    if len(arr) == r:
        cnt+=1
        vals[sum(arr)] = 1
        return

    for i in range(idx+1, len(matrix)):
        if visited[i] == 1: continue
        visited[i] = 1
        dfs(i, arr+[matrix[i]])
        visited[i] = 0


for r in range(1, N+1):
    dfs(-1, [])

idx = 1
while 1:
    if vals[idx] == 0:
        print(idx)
        break
    idx+=1