N, S = map(int, input().split(" "))
lst = list(map(int, input().split(" ")))

cnt = 0
visited = [0 for _ in range(N)]

r= 3

def dfs(idx, arr):
    global cnt
    if len(arr) == r:
        if sum(arr)==S: cnt+=1
        return arr

    for i in range(idx+1, len(lst)):
        if visited[i] == 1: continue
        visited[i] = 1
        dfs(i, arr + [lst[i]])
        visited[i] = 0

for r in range(1, N+1):
    dfs(-1, [])

print(cnt)