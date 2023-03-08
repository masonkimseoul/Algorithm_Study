d, n = map(int, input().split())
x, y = map(int, input().split())
result = [1, 1]
cnt = [[0, 0], [1, 1], [0, 1], [0, 0], [1, 0]]
m = 0
while n > 0:
    t = n % 10
    n //= 10
    result[0] += cnt[t][0] * pow(2, m)
    result[1] += cnt[t][1] * pow(2, m)
    m += 1
result[0] += x
result[1] += y
if 1 <= result[0] <= pow(2, d) and 1 <= result[1] <= pow(2, d):
    start = [1, 1]
    end = [pow(2, d), pow(2, d)]
    a, b = result
    answer = ''
    for _ in range(d):
        # print(start, end)
        xbaseline = (start[0] + end[0]) // 2
        ybaseline = (start[1] + end[1]) // 2
        # 1사분면
        if a > xbaseline and b > ybaseline:
            start = [xbaseline, ybaseline]
            answer += '1'
        # 2사분면
        if a <= xbaseline and b > ybaseline:
            start[1] = ybaseline
            end[0] = xbaseline
            answer += '2'
        # 3사분면
        if a <= xbaseline and b <= ybaseline:
            end = [xbaseline, ybaseline]
            answer += '3'
        # 4사분면
        if a > xbaseline and b <= ybaseline:
            start[0] = xbaseline
            end[1] = ybaseline
            answer += '4'
    print(answer)
else:
    print(-1)
