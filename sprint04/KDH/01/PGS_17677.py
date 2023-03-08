def solution(str1, str2):
    answer = 0

    str1_ = []
    str2_ = []
    for s in str1:
        if 'a' <= s <= 'z':
            s = chr(ord(s)-32)
        str1_.append(s)
    for s in str2:
        if 'a' <= s <= 'z':
            s = chr(ord(s)-32)
        str2_.append(s)
    if str1_ == str2_:
        return 65536

    str1__ = []
    str2__ = []
    for i in range(len(str1_)-1):
        if 'A' <= str1_[i] <= 'Z' and 'A' <= str1_[i+1] <= 'Z':
            str1__.append("".join(str1_[i:i+2]))
    for i in range(len(str2_)-1):
        if 'A' <= str2_[i] <= 'Z' and 'A' <= str2_[i+1] <= 'Z':
            str2__.append("".join(str2_[i:i+2]))

    set1 = 0
    set2 = 0
    for s in str1__:
        if s in str2__:
            set1 += 1
            str2__.remove(s)
    set2 = len(str1__) + len(str2__)

    answer = int((set1/set2)*65536)

    return answer
