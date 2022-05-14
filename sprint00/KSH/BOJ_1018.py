
def check_num_start_w(lst):
    num = 0
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if (i % 2 == 0):
                if (j%2==0 and lst[i][j]=='W'):
                    num += 1
                elif (j%2==1 and lst[i][j]=='B'):
                    num += 1
                else:
                    pass
            else:
                if (j%2==0 and lst[i][j]=='B'):
                    num += 1
                elif (j%2==1 and lst[i][j]=='W'):
                    num += 1
                else:
                    pass
    return num


def check_num_start_b(lst):
    num = 0
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if (i % 2 == 0):
                if (j%2==0 and lst[i][j]=='B'):
                    num += 1
                elif (j%2==1 and lst[i][j]=='W'):
                    num += 1
                else:
                    pass
            else:
                if (j%2==0 and lst[i][j]=='W'):
                    num += 1
                elif (j%2==1 and lst[i][j]=='B'):
                    num += 1
                else:
                    pass
    return num


if __name__ == "__main__":
    n, m = map(int, input().split())

    lst = []
    num = []

    for i in range(n):
        lst.append(list(input()))

    for i in range(n - 7):
        for j in range(m - 7):
            num.append(check_num_start_w([[lst[l][k] for k in range(j, j+8)] for l in range(i, i+8)]))
            num.append(check_num_start_b([[lst[l][k] for k in range(j, j+8)] for l in range(i, i+8)]))
    
    print(min(num))
