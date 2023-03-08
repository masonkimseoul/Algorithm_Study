n, s = map(int, input().split())
L = list(map(int, input().split()))
distance_list = [abs(s-i) for i in L]


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


if n == 1:
    print(distance_list[0])
else:
    ans = gcd(distance_list[0], distance_list[1])
    for i in distance_list:
        ans = gcd(ans, i)
    print(ans)
