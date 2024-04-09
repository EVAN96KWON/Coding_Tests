def solution(s):
    answer = [0, 0]

    while s != "1":
        answer[0] += 1  # round
        len_s = 0
        for i in s:
            # count zeroes
            if i == '0':
                answer[1] += 1
            # count length of ones
            else:
                len_s += 1
        s = str(bin(len_s)[2:])

    return answer


if __name__ == '__main__':
    print(solution("110010101001"))  # [3,8]
    print(solution("01110"))  # [3,3]
    print(solution("1111111"))  # [4,1]
