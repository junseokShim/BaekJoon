import math
from collections import deque

N = int(input())
M = int(input())
if M==0: f_list = []
else: f_list = [int(num) for num in input().split(" ")]

# 고장 안난 버튼
str_N = str(N)
buttons = [button for button in range(0, 10) if button not in f_list]

# 가장 가까운 수 찾기
# 앞자리부터 ㅎㅎ.
di = [-1, 1]

def bfs(num):
    q = deque()
    q.append(num)
    visited = [0]*(10)
    visited[num] = 1
    results = []
    while q:
        num = q.popleft()
        num = int(num)
        if num in buttons:
            results.append(str(num))
            #continue
        for d in di:
            nd = num+d
            if nd < 0 or nd >9: continue
            if visited[nd] == 1: continue
            visited[nd] = 1
            q.append(str(nd))
    return results


min_val = math.inf
min_len = math.inf
def dfs(start_num, depth):
    global min_val, min_len
    if depth == len(ord_lst)-1: 
        for n in ord_lst[depth]:
            min_val = min(min_val, abs(N-int(start_num+n)))
            if N-int(start_num+n)>=min_val and len(str(int(start_num+n)))<=min_len:
                min_val = N-int(start_num+n)
                min_len = len(str(int(start_num+n)))
                #print(min_val, start_num + n, min_len)
            #num_lst.append(start_num + n)
        return min_val, min_len
    for n in ord_lst[depth]:
        dfs(start_num+n, depth+1)
    
    return min_val, min_len

ord_lst = []
for i in range(len(str_N)):
    num = []
    if i == 0:
        num.append('0')
        num.extend([e for e in bfs(int(str_N[i])) if e != '0'])

    else:
        num = bfs(int(str_N[i]))
    ord_lst.append(num)

num_lst, l = dfs("", 0)
num1 = num_lst+l
num2 = abs(N-100)

print(min(num1, num2))