N = int(input())
series = list(map(int, input().split(" ")))
add, sub, mul, div = list(map(int, input().split(" ")))

max_num = -1000000000
min_num = 10000000000

def dfs(i, now):
    global max_num, min_num, add, sub, mul, div

    if i == N:
        max_num = max(max_num, now)
        min_num = min(min_num, now)

    else:
        if add > 0:
            add -= 1
            dfs(i+1, now + series[i])
            add += 1

        if sub > 0:
            sub -= 1
            dfs(i+1, now - series[i])
            sub += 1
        
        if mul > 0:
            mul -= 1
            dfs(i+1, now*series[i])
            mul += 1

        if div > 0:
            div -= 1
            dfs(i+1, int(now/series[i]))
            div += 1

dfs(1, series[0])

print(max_num)
print(min_num)

