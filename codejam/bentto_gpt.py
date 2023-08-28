def get_dist(p1, p2):
    c_elevator_dist = 0
    n_elevator_dist = 0

    if p1[0] != p2[0]:
        c_elevator, n_elevator = select_elevator(p1, p2)
        c_elevator_dist = get_dist(p1, c_elevator)
        n_elevator_dist = get_dist(p2, n_elevator)
        p1 = c_elevator
        p2 = n_elevator

    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]) + abs(p1[2] - p2[2]) + c_elevator_dist + n_elevator_dist

def select_elevator(p1, p2):
    min_dist = float('inf')
    c_elevators = [[p1[0], 1, 1], [p1[0], 1, L], [p1[0], W, 1], [p1[0], W, L]]
    n_elevators = [[p2[0], 1, 1], [p2[0], 1, L], [p2[0], W, 1], [p2[0], W, L]]

    c_min_elevator = []
    n_min_elevator = []

    for c_elevator, n_elevator in zip(c_elevators, n_elevators):
        if get_dist(c_elevator, p1) + get_dist(n_elevator, p2) <= min_dist:
            min_dist = get_dist(c_elevator, p1) + get_dist(n_elevator, p2)
            c_min_elevator = c_elevator
            n_min_elevator = n_elevator

    return c_min_elevator, n_min_elevator

def solve(floors):
    dp = [0 for _ in range(N+1)]

    for i in range(1, N + 1):
        min_dist = float('inf')
        min_index = 0

        for idx in range(i, N+1):
            if get_dist(floors[i-1], floors[idx]) < min_dist:
                min_dist = get_dist(floors[i-1], floors[idx])
                min_index = idx

        # swap
        floors[i], floors[min_index] = floors[min_index], floors[i]

        dp[i] = dp[i-1] + min_dist

    return dp

T = int(input())  # 테스트 케이스 수
answers = []

for _ in range(T):
    F, W, L, N = map(int, input().split())
    Sz, Sx, Sy = map(int, input().split())
    floors = [[e for e in map(int, input().split(" "))] for _ in range(N)]

    floors.sort(key=lambda x:x[0])
    floors = [[Sz, Sx, Sy]] + floors

    answers.append(solve(floors))

# 각 테스트 케이스 별로 정답 출력
for ans in answers:
    print(ans[-1])
