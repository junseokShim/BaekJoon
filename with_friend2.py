from itertools import combinations

T = int(input())

# N : 집의 수
# Pa : 창고 A의 위치
# Pb : 창고 B의 위치

def min_delivery_distribution(Pa, Pb, lst):

    dist_Pa = 0 # Albert가 이동한 거리 
    dist_Pb = 0 # Bob이 이동한 거리
    if Pa > Pb:
        tmp = Pb
        Pb = Pa
        Pa = tmp
        print(Pa,Pb)
        
    lst = sorted(lst)
    mid = int((Pa + Pb)/2)

    A_deliveries = [a_h for a_h in lst if a_h < mid]
    B_deliveries = [b_h for b_h in lst if b_h > mid]

    total_distance_A = sum(2 * abs(x - Pa) for x in A_deliveries)
    total_distance_B = sum(2 * abs(x - Pb) for x in B_deliveries)

    mid_count = lst.count(mid)
    total_distance_mid = sum(2 * abs(mid - Pb) for _ in range(mid_count))

    min_dist = total_distance_A + total_distance_B + total_distance_mid

    if mid_count % 2 ==1:
        if total_distance_A > total_distance_B: total_distance_B += 2 * abs(mid - Pb)
        else: total_distance_A += 2 * abs(mid - Pb)
    
    min_diff_dist = abs(total_distance_A - total_distance_B)

    # 결과 반환
    return min_dist, min_diff_dist

answers = []
for i in range(T):
    N, Pa, Pb = map(int, input().split(" "))
    lst = [int(e) for e in input().split(" ")]
    answers.append(min_delivery_distribution(Pa, Pb, lst))

for total_distance, distance_diff in answers:
    print(total_distance, distance_diff)
