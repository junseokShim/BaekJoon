from itertools import permutations
K = int(input())
inequality_signs = input().split(" ")

max_nums = list(range(10-K-1,10))
min_nums = list(range(0, K+1))

max_val = '0'*(K+1)
min_val = '9'*(K+1)

visited_max = [0 for _ in range(K+1)]
visited_min = [0 for _ in range(K+1)]


def DFS_max(cnt, lst):

    global max_val

    if cnt>=2:
        if inequality_signs[cnt-2] == "<" and lst[cnt-2]>lst[cnt-1]:
            return

        if inequality_signs[cnt-2] == ">" and lst[cnt-2]<lst[cnt-1]:
            return

    if cnt == len(max_nums):
        max_val = max(max_val, "".join(map(str, lst[:])))
        return

    for i, val in enumerate(max_nums):
        if visited_max[i] == 1: continue
        lst.append(val)
        visited_max[i] = 1
        
        DFS_max(cnt+1, lst)

        lst.pop()
        visited_max[i] = 0


def DFS_min(cnt, lst):
    
    global min_val

    if cnt>=2:
        if inequality_signs[cnt-2] == "<" and lst[cnt-2]>lst[cnt-1]:
            return

        if inequality_signs[cnt-2] == ">" and lst[cnt-2]<lst[cnt-1]:
            return

    if cnt == len(min_nums):
        min_val = min(min_val, "".join(map(str, lst[:])))
        return

    for i, val in enumerate(min_nums):
        if visited_min[i] == 1: continue
        lst.append(val)
        visited_min[i] = 1
        
        DFS_min(cnt+1, lst)

        lst.pop()
        visited_min[i] = 0


DFS_max(0, [])
DFS_min(0, [])

print(max_val)
print(min_val)
