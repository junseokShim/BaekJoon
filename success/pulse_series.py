def solution(sequence):
    
    sequence = [0] + sequence
    
    l = len(sequence)
    
    sequence = [(-1)**(i)*sequence[i] for i in range(l)]
    
    # dp[i] = i까지 탐색했을 때의 최대값
    # dp1 -> -1부터 시작하는 연속 펄스 수열 사용
    # dp2 -> +1부터 시작하는 연속 펄스 수열 사용
    
    dp1 = [0]*(len(sequence))
    dp2 = [0]*(len(sequence))
    
    dp1[1] = sequence[1]
    dp2[1] = sequence[1]
    
    for i in range(2, len(sequence)):
        dp1[i] = min(dp1[i-1] + sequence[i], sequence[i])
        dp2[i] = max(dp2[i-1] + sequence[i], sequence[i])
           
    return max(abs(min(dp1)), abs(max(dp2)))