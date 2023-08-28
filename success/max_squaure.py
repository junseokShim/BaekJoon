import math

N, M = map(int, input().split(' '))
matrix = [[0 for _ in range(M+1)]]+[[0]+[int(e) for e in list(input())] for _ in range(N)]

# dp[i][j] matrix[i][j]==1일때, i, j에서의 가장 큰 정사각형 크기
dp = [[0 for _ in range(M+1)] for __ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, M+1):
        if matrix[i][j] == 1:

            side_num = int(math.sqrt(dp[i-1][j-1]))
            penalty_num = side_num
            for num in range(1, side_num+1):
                if matrix[i-num][j] == 0:
                    break
                
                if matrix[i][j-num] == 0:
                    break

                penalty_num -= 1
                
            dp[i][j] = int(math.pow(math.sqrt(dp[i-1][j-1])+1-penalty_num, 2))

print(max(map(max,dp)))