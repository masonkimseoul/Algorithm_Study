import math
x, y, c = map(float, input().split())

r = min(x, y)
l = 0

while abs(l-r) >= 0.001:
    d = (l+r) / 2
    h1 = math.sqrt(pow(x, 2) - pow(d, 2))
    h2 = math.sqrt(pow(y, 2) - pow(d, 2))
    h = h1 * h2 / (h1 + h2)
    if h <= c:
        r = d
    else:
        l = d
print(round(d, 3))
