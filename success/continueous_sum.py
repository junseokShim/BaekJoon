import math

n = int(input())
nums = [0]+[int(i) for i in input().split(" ")]
dp = [0]*(n+1)
dp[1] = nums[1]

for i in range(2, n+1):
    dp[i] = max(dp[i-1] + nums[i], nums[i])

dp = dp[1:]
max_val = max(dp)
print(max_val)