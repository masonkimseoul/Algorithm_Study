def solution(cap, n, deliveries, pickups):
    answer = 0
    C = 0
    D = n-1
    P = n-1
    SD = sum(deliveries)
    SP = sum(pickups)
    while SD != 0 or SP != 0:
        # 배달 완료된 집 탐색에서 제외하기
        for i in range(D, -1, -1):
            if deliveries[i] == 0:
                D -= 1
            else:
                break
        # 픽업 완료된 집 탐색에서 제외하기
        for i in range(P, -1, -1):
            if pickups[i] == 0:
                P -= 1
            else:
                break
        # 배달 남은 만큼 트럭에 담는다
        if cap <= SD:
            C = cap
            SD -= cap
        else:
            C = SD
            SD = 0
        # 수거나 배달중 제일 먼 곳 까지 택배 출발
        if D < P:
            T = P
        else:
            T = D
        # 뒤에서부터 배달
        for i in range(D, -1, -1):
            # 배달 하고 트럭에 박스가 남아있는 경우
            if C > deliveries[i]:
                C = C - deliveries[i]
                deliveries[i] = 0
            # 배달 하고 트럭에 박스가 남아있지 않는 경우
            else:
                deliveries[i] = deliveries[i] - C
                C = 0
                break
        # 수거 뒤에서부터 수거
        for i in range(P, -1, -1):
            # 수거 하고 택배에 더 실을 수 있는 경우
            if cap > pickups[i] + C:
                C += pickups[i]
                SP -= pickups[i]
                pickups[i] = 0
            # 트럭에 짐을 실으면 트럭이 가득 차는 경우
            else:
                pickups[i] -= (cap - C)
                SP -= (cap-C)
                C = cap
                break

        answer += (T+1)*2
    return answer


print(solution(2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0]))
