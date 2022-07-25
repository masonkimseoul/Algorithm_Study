def solution(n):
    nums = ['1', '2', '4']
    ans = []
    while n > 0:
        n, r = divmod(n-1, 3)
        ans.append(nums[r])

    ans_ = "".join(reversed(ans))
    return ans_
