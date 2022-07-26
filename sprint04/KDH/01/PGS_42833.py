def solution(number, k):
    answer = []
    for num in number:
        if not answer:
            answer.append(num)
            continue

        if k > 0:
            while answer:
                if answer[-1] < num:
                    answer.pop()
                    k -= 1
                    if k == 0:
                        break
                else:
                    break

        answer.append(num)

    answer = ''.join(answer[:len(number)-k])

    return answer
