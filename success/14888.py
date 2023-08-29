N = int(input())
series = list(map(int, input().split(" ")))
operators = list(map(int, input().split(" ")))

ops = ""
for idx in range(len(operators)):

    if idx == 0: ops += "+"*operators[idx]
    elif idx == 1: ops += "-"*operators[idx]
    elif idx == 2: ops += "*"*operators[idx]
    elif idx == 3: ops += "/"*operators[idx]

ops = list(ops)

max_num = -1*float("inf")
min_num = float("inf")

visited_max = [0 for _ in range(N)]
visited_min = [0 for _ in range(N)]

def max_dfs(num, lst):

    global max_num

    if len(lst) == N-1:
        max_num = max(num, max_num)
        return

    for i, val in enumerate(ops):
        if visited_max[i] == 1: continue
        lst.append(val)
        visited_max[i] = 1

        if val == "+":      max_dfs( num+series[len(lst)], lst)
        elif val == "-":    max_dfs( num-series[len(lst)], lst)
        elif val == "*":    max_dfs( num*series[len(lst)], lst)
        else:               max_dfs(int(num/series[len(lst)]), lst)

        lst.pop()

        visited_max[i] = 0


def min_dfs(num, lst):
    
    global min_num

    if len(lst) == N-1:
        min_num = min(num, min_num)
        return

    for i, val in enumerate(ops):
        if visited_min[i] == 1: continue
        lst.append(val)
        visited_min[i] = 1

        if val == "+":      min_dfs( num+series[len(lst)], lst)
        elif val == "-":    min_dfs( num-series[len(lst)], lst)
        elif val == "*":    min_dfs( num*series[len(lst)], lst)
        else:               min_dfs(int(num/series[len(lst)]), lst)

        lst.pop()
        visited_min[i] = 0

max_dfs(series[0], [])
min_dfs(series[0], [])

print(max_num)
print(min_num)

