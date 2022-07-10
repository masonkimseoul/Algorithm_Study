

def dfs(val, lst, visited, target):
    
    global cnt

    if val == target:
        return True

    for new_idx, i in enumerate(lst):
        if val in i and visited[new_idx] == 0:
            a, b = i
            if a == val:
                new_val = b
            else:
                new_val = a
            visited[new_idx] = 1
            # cnt += 1

            if dfs(new_val, lst, visited, target):
                cnt += 1
                return True

    return False

if __name__ == "__main__":
    
    m = int(input())
    a, b = map(int, input().split())

    n = int(input())
    lst = []
    cnt = 0
    visited = [0 for i in range(n)]
    for i in range(n):
        p, q = map(int, input().split())
        lst.append([p, q])

    dfs(a,lst, visited, b)

    if cnt == 0:
        cnt = -1
    print(cnt)