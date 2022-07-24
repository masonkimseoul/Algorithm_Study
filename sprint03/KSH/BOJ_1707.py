

import sys

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def dfs(n, color, graph, visited):
    visited[n] = color
    for i in graph[n]:
        if visited[i] == -1:
            if dfs(i, (color + 1)%2, graph, visited) == False:
                return False
        else:
            if visited[i] == color:
                return False
    return True

if __name__ == "__main__":

    n = int(input())
    for i in range(n):
        lst = []
        a, b = map(int, input().split())
        for j in range(b):
            lst.append(list(map(int, input().split())))
        graph = [[] for j in range(a+1)]
        visited = [-1 for i in range(a+1)]

        for i in lst:
            graph[i[0]].append(i[1])
            graph[i[1]].append(i[0])
        
        flag = True
        for i in range(1, a+1):
            if visited[i] == -1:
                if dfs(i, 0, graph, visited) == False:
                    flag = False
                    break
        
        if flag == False:
            print("NO")
        else:
            print("YES")