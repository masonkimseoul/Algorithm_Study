import sys
input = sys.stdin.readline

N = int(input())
frame = []
total = int(input())
candidates = list(map(int, input().split()))

# 추천 횟수
students = [0] * (101)

for i in range(len(candidates)):
    if candidates[i] in frame:
        students[candidates[i]] += 1
    else:
        if len(frame) == N:
            min_ = total+1
            stu_ = -1
            for stu in frame:
                if students[stu] < min_:
                    min_ = students[stu]
                    stu_ = stu
            frame.remove(stu_)
            students[stu_] = 0

        frame.append(candidates[i])
        candidates[i] += 1

print(*(sorted(frame)))
