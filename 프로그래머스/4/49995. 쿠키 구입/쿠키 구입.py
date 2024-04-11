def solution(cookie):
    answer = 0

    for i in range(len(cookie) - 1):
        left, right = i, i + 1
        l_sum, r_sum = cookie[left], cookie[right]

        while True:
            if l_sum == r_sum:
                answer = max(answer, l_sum)

            if left > 0 and l_sum <= r_sum:
                left -= 1
                l_sum += cookie[left]
            elif right < len(cookie) - 1 and l_sum >= r_sum:
                right += 1
                r_sum += cookie[right]
            else:
                break

    return answer
