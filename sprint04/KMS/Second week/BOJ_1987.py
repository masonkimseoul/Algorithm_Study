import copy
R, C = map(int, input().split())
matrix = [list(input()) for _ in range(R)]
p =0
def dfs(x,y,count):
    global p
    global a
    nx = [1, -1 , 0, 0]
    ny = [0, 0, 1, -1]
    p = max(p,count)
    for i in range(4):
        rx = nx[i] + x
        ry = ny[i] + y
        if 0<= rx <= C-1 and 0 <= ry <= R-1 and a[ord(matrix[ry][rx])-ord('A')] == 0:
            a[ord(matrix[ry][rx])-ord('A')] = 1
            dfs(rx,ry,count +1)
            a[ord(matrix[ry][rx])-ord('A')] = 0
a = [0] * 26
a[ord(matrix[0][0]) -ord('A')] = 1
dfs(0,0,1)
print(p)