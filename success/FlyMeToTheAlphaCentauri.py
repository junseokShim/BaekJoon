import math

## 입력 ##
T = int(input())

positions = []
for _ in range(T):
    s, e = map(int, input().split(" "))
    positions.append([s, e])


## 풀이 ##
'''
DFS는 사용하면 안됨
ran이 0~2**31의 범위를 가지기 때문에 Recursive Error가 발생해 
DFS 사용시, Run time Error가 발생함

추가로, 리스트나 배열을 사용할 경우에는 메모리 초과로 인해 사용할 수 없음
(배열을 사용할 경우 길이가 2**31인 배열을 생성해야하므로 메모리 초과 에러가 발생함)
'''

def func(t):
    if t == 1: return 1
    elif t == 2: return 2

    s = 0
    c = -1
    i = 0

    while 1:

        if s >= t: break
        for _ in range(2):
            s += i
            if s >= t:
                break
            c += 1
        i += 1
        
    return c


for position in positions:
    ran = position[1]-position[0]
    print(func(ran))