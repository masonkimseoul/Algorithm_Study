def solution(scores):
    A, B = scores[0]
    T1 = scores
    T1.sort(key=lambda x: -sum(x))
    # 완호가 인센티브를 못받는 경우
    for a, b in T1:
        if a > A and b > B:
            return -1
    Index = len(T1) - 1
    for idx, data in enumerate(T1):
        a, b = data
        if a > A and b > B:
            return -1
        if a+b <= A+B:
            Index = idx
            break
    # 점수 낮은 애들 제거
    T = T1[:Index]
    # 인센티브를 못받는 사람 L리스트에 인덱스 담기
    L = []
    for idx, data in enumerate(T1):
        a, b = data
        start = idx
        end = len(T1)-1
        while start <= end:
            mid = (start + end) // 2
            if T1[mid][0] <= a:
                start = mid + 1
            else:
                end = mid - 1
        for i in range(start, len(T1)):
            aa, bb = T1[i]
            if a < aa and b < bb:
                L.append(idx)
                break
    # 리스트에서 인센티브 못받는 사람들 제거
    for i in L:
        T1.pop(i)

    T = [data for idx, data in enumerate(T) if idx not in L]
    print(T)
    if not T:
        return 1
    a, b = T[0]
    cnt = 1
    # 완호가 일등일 때
    if a+b <= A+B:
        return cnt
    prev = 100001
    for idx, data in enumerate(T):
        a, b = data
        # 이전 점수랑 같은경우 순위 변동 X
        if a+b == prev:
            continue
        # 이전 점수 보다 작은경우
        else:
            cnt = idx + 1
        if a+b <= A+B:
            return cnt
    return cnt + 1
