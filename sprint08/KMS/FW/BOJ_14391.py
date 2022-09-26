# import sys
# col, row = map(int, input().split())
# matrix = []
# for i in range(col):
#     matrix.append(input())

# # 1 -> col, 2 -> row
# col_sum = 0
# row_sum = 0

# # 매트릭스 정제
# while row_sum ==0:
#     for i in range(row):
#         row_sum += int(matrix[0][i])
#     if row_sum == 0:
#         del matrix[0]
#         col -= 1
# while col_sum == 0:
#     for i in range(col):
#         col_sum += int(matrix[i][0])
#     if col_sum == 0:
#         for i in range(col):
#             matrix[i] = matrix[i][1:-1]
#         row -= 1
        
# # flag 1 -> col, 2 -> row
# if col > row:
#     flag = 1
# elif col < row:
#     flag = 2
# # col = row
# else:
#     if col_sum > row_sum:
#         flag = 2
#     else:
#         flag = 1
# result = 0
# # row < col
# if flag == 1:
#     for i in range(row):
#         t = ''
#         for j in range(col):
#             t += matrix[j][i]
#         result += int(t)
# # row > col
# else:
#     for i in range(col):
#         result += int(matrix[i])
    
# print(int(result))

N,M=map(int,input().split())
room=[list(map(int,input().rstrip())) for _ in range(N)]
answer=0
for i in range(1<<N*M):
    total=0
    print(i)
    # #가로를 보는 경우
    # for sx in range(N):
    #     tmp_ga=0

    #     for sy in range(M):
    #         idx=sx*M+sy
    #         #비트가 맞으면
    #         if i&(1<<idx)!=0:
    #             tmp_ga=10*tmp_ga+room[sx][sy]
    #         else:
    #             total+=tmp_ga
    #             tmp_ga=0
    #     total+=tmp_ga
    # #세로를 보는 경우
    # for sy in range(M):
    #     tmp_sa = 0

    #     for sx in range(N):
    #         idx = sx * M + sy
    #         # 비트가 맞으면
    #         if i & (1<<idx) == 0:
    #             tmp_sa = 10 * tmp_sa + room[sx][sy]
    #         else:
    #             total += tmp_sa
    #             tmp_sa = 0
    #     total+=tmp_sa

    # answer=max(answer,total)
# print(answer)