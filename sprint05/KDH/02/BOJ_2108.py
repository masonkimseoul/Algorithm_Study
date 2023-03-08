from collections import defaultdict
from collections import Counter
import sys
input = sys.stdin.readline

N = int(input())

nums = []
for _ in range(N):
    nums.append(int(input()))

if N == 1:
    print(nums[0])
    print(nums[0])
    print(nums[0])
    print(0)

else:
    nums.sort()

    print(round(sum(nums) / N))
    print(nums[N//2])

    # 시간 초과
    # dic = defaultdict()
    # for n in list(set(nums)):
    #     dic[n] = nums.count(n)
    # dic_ = sorted(dic.items(), key=lambda x: (x[1], -x[0]), reverse=True)
    # if dic_[0][1] == dic_[1][1]:
    #     print(dic_[1][0])
    # else:
    #     print(dic_[0][0])
    counts = Counter(nums).most_common(2)
    if (counts[0][1] == counts[1][1]):
        print(counts[1][0])
    else:
        print(counts[0][0])

    print(nums[-1] - nums[0])
