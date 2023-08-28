def min_delivery_distribution(P_A, P_B, X):
    N = len(X)
    
    # 모든 집을 두 창고로부터의 거리에 따라 정렬
    sorted_houses = sorted(X, key=lambda x: abs(x - P_A) - abs(x - P_B))
    
    # 두 사람이 각자 배달할 집들을 선택
    A_deliveries = sorted_houses[:N // 2]
    B_deliveries = sorted_houses[N // 2:]
    
    # 두 사람의 이동 거리 계산
    total_distance_A = sum(2 * abs(x - P_A) for x in A_deliveries) + 2 * P_A
    total_distance_B = sum(2 * abs(x - P_B) for x in B_deliveries) + 2 * P_B
    
    # 결과 반환
    return total_distance_A + total_distance_B, abs(total_distance_A - total_distance_B)

# 예시 입력
P_A = 0


# 예시 입력
P_A = 0
P_B = 100
X = [10, 20, 50, 60]

total_distance, distance_diff = min_delivery_distribution(P_A, P_B, X)
print("두 사람의 이동 거리 합:", total_distance)
print("두 사람의 이동 거리 차이:", distance_diff)