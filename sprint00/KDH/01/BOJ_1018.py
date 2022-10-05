import sys
input = sys.stdin.readline

N, M = map(int, input().split())

board = [input().rstrip() for _ in range(N)]

ans = N*M
for i in range(0, N-7):
    for j in range(0, M-7):
        W_ = 0 # start with 'W'
        B_ = 0 # start with 'B'
        for x in range(i, i+8):
            for y in range(j, j+8):
                if (x+y) % 2 == 0:
                    if board[x][y] != 'W':
                        W_ += 1
                    if board[x][y] != 'B':
                        B_ += 1
                else:
                    if board[x][y] != 'B':
                        W_ += 1
                    if board[x][y] != 'W':
                        B_ += 1
        print(W_)
        print(B_)
        tmp = min(W_, B_)
        ans = min(ans, tmp)
        if ans == 0:
            break
        
print(ans)