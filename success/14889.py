from itertools import combinations, permutations

N = int(input())
S = [[0 for _ in range(N+1)]] + [[0] + list(map(int, input().split(" "))) for _ in range(N)]

total = sum([sum(S[j]) for j in range(len(S))])

min_diff = float("inf")
chosen = []

man = [i for i in range(1, N+1)]

for team_a in combinations(man, int(N/2)):
    score_a = 0
    score_b = 0

    team_a = list(team_a)
    team_b = [e for e in man if e not in team_a]
    for i in range(len(team_a)):
        for j in range(i+1, len(team_a)):
            score_a += S[team_a[i]][team_a[j]]
            score_a += S[team_a[j]][team_a[i]]
            score_b += S[team_b[i]][team_b[j]]
            score_b += S[team_b[j]][team_b[i]]
    min_diff = min(abs(score_b-score_a), min_diff)

        
print(min_diff)
