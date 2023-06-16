N = int(input())

matrix = [[""]*(N+2)]
for _ in range(N):
    matrix.append([""] + list(input()) + [""])

matrix.append([[""]*(N+2)])


from collections import deque

def func(s):
    '''
    desc : get max len
    input : "aaaabb"
    output : 4
    '''
    max_len = 1
    l = 1
    for i in range(len(s)-1):
        if s[i] == s[i+1]: 
            l+=1
        else:
            l = 1
        max_len = max(l, max_len)
    return max_len


q = deque()
d = [[-1, 0], [1, 0], [0, -1], [0, 1]] # 좌,우,하,상
q.append([1,1]) # 1,1부터 시작

visited = [[0]*(N+2) for _ in range(N+2)] 
visited[1][1] = 1

def col_str():
    l = 0
    for j in range(N+1):
        s = "".join(matrix[j])
        l = max(l,func(s))
    return l

def row_str():
    l = 0
    for j in range(N+1):
        s = "".join([matrix[i][j] for i in range(N+1)])
        l = max(l, func(s))
    return l


## bfs
max_len = 0

while q:
    x, y = q.popleft()
    for dx, dy in d:
        nx, ny = x + dx, y + dy

        if nx > N or nx <= 0: continue
        if ny > N or ny <= 0: continue
        if visited[nx][ny] == 1: continue

        #print([x,y], [nx,ny])
        # x, y와 nx, ny 자리의 element를 변경
        
        # 검사
        if matrix[nx][ny] == matrix[x][y]:
            visited[x][y] = 1
            if [nx, ny] not in q:
                q.append([nx, ny])
            continue

        swap = matrix[nx][ny]
        matrix[nx][ny] = matrix[x][y]
        matrix[x][y] = swap

        max_len = max(max_len, col_str(), row_str())

        # x, y 원래대로
        swap = matrix[nx][ny]
        matrix[nx][ny] = matrix[x][y]
        matrix[x][y] = swap

        visited[x][y] = 1
        if [nx, ny] not in q:
            q.append([nx, ny])


print(max_len)