from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 1
    matrix = [[0]*101 for _ in range (101)]
    
    
    # 매트릭스 생성
    for rect in rectangle:
        x1 = rect[0]*2
        y1 = rect[1]*2
        x2 = rect[2]*2
        y2 = rect[3]*2
        for x in range(x1,x2+1):
            for y in range(y1,y2+1):
                matrix[y][x] = 1
    # 상하좌우 확인 0있으면 1리턴 없으면 0 리턴
    def check(x,y):
        nx = [1,-1,0,0]
        ny = [0,0,1,-1]
        if x == 2 or y == 2 or x == 100 or y ==100:
            return 1
        for i in range(4):
                rx = nx[i] + x
                ry = ny[i] + y
                if 2<= rx <= 100 and 2 <= ry<= 100 and matrix[ry][rx] == 0:
                    return 1
        return 0
    # inside
    def corner(x,y):
        nx = [1,1,-1,-1]
        ny = [1,-1,1,-1]
        for i in range(4):
                rx = nx[i] + x
                ry = ny[i] + y
                if 2<= rx <= 100 and 2<= ry<= 100 and matrix[ry][rx] ==0:
                    return 1
        return 0
    
    def bfs(x, y, ix,iy):
        q = deque()
        index = deque()
        co = deque()
        count = 0
        matrix[y][x] = 2
        q.append((x,y,count))
        nx = [1,-1,0,0]
        ny = [0,0,1,-1]
        while q:
            x,y,count= q.popleft()
            if x == ix and y ==iy:
                return count
            for i in range(4):
                rx = nx[i] + x
                ry = ny[i] + y
                if 2<=rx <=100 and 2<= ry <= 100 and matrix[ry][rx] == 1:
                    if check(rx,ry) == 0 and corner(rx,ry) == 1:
                        co.append((rx,ry))
                    elif check(rx,ry) == 1:
                        index.append((rx,ry))
                    
            if co:
                cx,cy = co.popleft()
                matrix[cy][cx] = 2
                q.append((cx,cy,count+1))
                while index:
                    index.popleft()
            else:
                while index:
                    cx,cy = index.popleft()
                    matrix[cy][cx] = 2
                    q.append((cx,cy,count+1))
                
                        
        return -1
    
    answer = bfs(characterX*2, characterY*2,itemX*2, itemY*2)
    
    return answer/2






