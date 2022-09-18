import sys
input = sys.stdin.readline

M = int(input())

nums = [i for i in range(1, 21)]
S = set()
for _ in range(M):
    str_ = input()
    
    if str_ == "all\n":
        S = set(nums)
        continue
    if str_ == "empty\n":
        S = set()
        continue
    
    fun, num = str_.split(" ")
    num = int(num)
    
    if (fun == "add" or fun == "toggle") and num not in S:
        S.add(num)
    elif (fun == "remove" or fun == "toggle") and num in S:
        S.remove(num)
    elif fun == "check":
        if num in S :
            print("1")
        else:
            print("0")