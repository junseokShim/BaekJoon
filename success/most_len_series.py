N = int(input())
arr = [int(num) for num in input().split(" ")]


# dp --> i까지 왔을 떄, 합의 최대
# 현재 배열 값보다 작은 값(인덱스)의 dp최댓값을 더하면 dp[i]를 구할 수 있음
dp = [1]*(N)

for i in range(1, len(arr)):
    lst = [dp[j] for j in range(len(arr[:i])) if arr[i] > arr[j]]

    if len(lst) == 0:
        continue

    else:
        dp[i] = max(lst) + 1

print(max(dp))