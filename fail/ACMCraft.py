
# ================================================================================ #

T = int(input())

answers = []

for _ in range(T):
    N, K = map(int, input().split(" "))
    d_list = [0] + [int(e) for e in list(input().split(" "))]
    rules = [[int(e) for e in list(input().split(" "))] for _ in range(K)]
    W = int(input())

    MAX = 100
    dp = [0]*(MAX+1)
    dp[1] = d_list[1]

    #rules.sort(key=lambda x : x)

    for i in range(2, MAX+1): # i는 dp index임
        j = 1
        max_val = 0
        while j < i:
            if [j,i] in rules:
                max_val = max(max_val, dp[j]+d_list[i])
            j += 1

        dp[i] = max_val

    answers.append(dp[W])

for answer in answers:
    print(answer)



# ================================================================================ #

from collections import deque

T = int(input())
answers = []

for _ in range(T):
    N, K = map(int, input().split(" "))

    d_list = [0] + [int(e) for e in list(input().split(" "))]
    rules = [] # 건설 순서 규칙을 저장하는 list

    #  i번째 건물의 부모노드 개수를 저장하는 array
    #  check_array[i] = -1 일 경우, 부모 노드가 없다고 판단
    #  즉, bfs 사용시 종료조건으로 사용하기 위함

    dp = [0]*(N+1)
    check_array = [0] * (N+1) 

    for _ in range(K):
        a, b = map(int, input().split(" "))
        rules.append([a,b])
        check_array[b] += 1


    q = deque()
    for i in range(len(check_array)):
        if check_array[i] == 0:
            q.append(i)
            dp[i] = d_list[i]
            check_array[i] = -1

    W = int(input())


    while q:
        current_building = q.popleft()
        # if current_building == W:
        #     break

        for rule in rules:
            if current_building == rule[0]:
                next_building = rule[1]
                check_array[next_building] -= 1 # 부모노드 하나를 끊어줌
                if check_array[next_building] == 0:
                    check_array[next_building] = -1 # 부모노드가 없음을 의미
                q.append(next_building)
                dp[next_building] = max(dp[next_building], \
                    d_list[next_building], \
                    dp[current_building]+d_list[next_building])

            #dp[next_building] = max_val
    
    answers.append(dp[W])


for answer in answers:
    print(answer)