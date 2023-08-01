from collections import deque

N, M = map(int, input().split(" "))
matrix = [[0]*(M+2)]
for _ in range(N):
    lst = [0] + [int(e) for e in input().split(" ")] + [0]
    matrix.append(lst)
matrix.append([0]*(M+2))

visited = [[0]*(M+2) for _ in range(N+2)]

def get_sum(c):
    s = 0
    for cl in c:
        s+=sum(cl)
    return s

def get_lst(l1, l2):
    c = []
    for ae, be in zip(l1, l2):
        lst = []
        for e1, e2 in zip(ae, be):
            if e2 == 0: e1 = 0
            lst.append(e1)
        c.append(lst)
    #print(c)
    return get_sum(c)
    

d = [[-1,0],[1,0],[0,-1],[0,1]]

max_val = 0

def tetrimino(n, m, visited, length):
    global max_val
    visited[n][m] = 1

    print("==================================")
    for v in visited:
        print(v)
    print("==================================")
    for dn, dm in d:
        nn, nm = n+dn, m+dm
        if nn <= 0 or nn > N: 
            visited[n][m] = 0
            continue
        if nm <= 0 or nm > M: 
            visited[n][m] = 0
            continue
        if visited[nn][nm] == 1: continue

        if length == 4:
            max_val = max(max_val, get_lst(matrix, visited))

        else:
            length += 1
            tetrimino(nn, nm, visited, length)
        

    return max_val

print(tetrimino(4,5,visited,1))
print(matrix[4][5])

# for m in range(M+2):
#     for n in range(N+2):
#         print(matrix[n][m])
#         print(visited[n][m])

# for v in visited:
#     print(v)

# for m in matrix:
#     print(m)