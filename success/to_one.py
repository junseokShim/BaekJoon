X = int(input())

dp = [0]*1000001

dp[0] = 0
dp[1] = 0
dp[2] = 1
dp[3] = 1

for idx in range(4, X+1):

    if idx%3==0 and idx%2==0:
        dp[idx] = min(1 + dp[idx//3], 1 + dp[idx//2], 1 + dp[idx-1])
    
    elif idx%3 == 0:
        dp[idx] = min(1 + dp[idx//3], 1 + dp[idx-1])

    elif idx%2 == 0:
        dp[idx] = min(1 + dp[idx//2], 1 + dp[idx-1])

    else:
        dp[idx] = 1 + dp[idx-1]

print(dp[X])