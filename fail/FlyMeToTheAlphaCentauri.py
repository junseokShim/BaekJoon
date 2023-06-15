import math

## 입력 ##
T = int(input())

positions = []
for _ in range(T):
    s, e = map(int, input().split(" "))
    positions.append([s, e])


## 풀이 ##
'''
DFS를 사용해 풀이를 할 경우, RecursionError가 발생할 수 있음
따라서 DFS가 아닌 다른 알고리즘을 사용해야함
'''

def dfs(ck, sum, count, total_range):
    global min_count

    if sum==total_range :
        if ck == 1 or ck == 2:
            min_count = min(min_count, count+1)
            return min_count

    for nk in [ck-1, ck, ck+1]:
        if nk <= 1: 
            nk = 1

        n_sum = sum + nk
        if n_sum > total_range:
            break

        dfs(nk, n_sum, count+1, total_range)
        
    return min_count


for position in positions:
    e = position[1]
    s = position[0]
    total_range = abs(e-s-1)
    min_count = math.inf
    print(dfs(1, 1, 1, total_range))