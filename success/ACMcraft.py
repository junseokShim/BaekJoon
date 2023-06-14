import sys
from collections import deque

input = sys.stdin.readline

T = int(input())
answers = []

for _ in range(T):
    N, K = map(int, input().split())
    
    d_list = [int(e) for e in input().split()]
    rules = []

    #  i번째 건물의 부모노드 개수를 저장하는 array
    #  check_array[i] = -1 일 경우, 부모 노드가 없다고 판단
    #  즉, bfs 사용시 종료조건으로 사용하기 위함
    dp = [0]*(N+1)
    check_array = [0] * (N+1) 

    for _ in range(K):
        a, b = map(int, input().split())
        rules.append((a, b))
        check_array[b] += 1

    q = deque()
    for i in range(1, N+1):
        if check_array[i] == 0:
            q.append(i)
            dp[i] = d_list[i-1]
            check_array[i] = -1

    W = int(input())

    while q:
        current_building = q.popleft()

        for a, b in rules:
            ## 탈출조건 안만들어주면 시간초과가 발생함
            if check_array[b] == -1: continue
            if a == current_building:
                check_array[b] -= 1
                if check_array[b] == 0:
                    q.append(b)
                    check_array[b] = -1

                dp[b] = max(dp[b], dp[a]+d_list[b-1])

    answers.append(dp[W])

for answer in answers:
    print(answer)