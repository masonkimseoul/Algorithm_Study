def targetNumber(numbers, target,i, val):
    cnt=0
    if len(numbers)==i:
        if val==target:
            return cnt+1
        return cnt
    cnt+=targetNumber(numbers, target, i + 1, val + numbers[i])
    cnt+=targetNumber(numbers, target, i + 1, val - numbers[i])

    return cnt

def solution(numbers, target):
    return targetNumber(numbers,target,0,0)

print(solution([4,1,2,1],4))