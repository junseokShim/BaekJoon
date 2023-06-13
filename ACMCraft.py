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