def solution(number, k):
    number = list(number)
    deleted_cnt = 0

    while deleted_cnt != k:
        print(number)
        for i in range(len(number) - 1):
            print(i, number[i], number[i] < number[i + 1])
            if i == len(number) - 2:
                number.pop(i) if number[i] < number[i + 1] else number.pop(i + 1)
                deleted_cnt += 1

            if number[i] is '9' and number[i] == number[i + 1]:
                number.pop(i)
                deleted_cnt += 1
                break

            if number[i] < number[i + 1]:
                number.pop(i)
                deleted_cnt += 1
                break

    return ''.join(number)

# 시간초과 8번 10번 테스트케이스

if __name__ == '__main__':
    print(solution("1924", 2))  # "94"
    print(solution("1231234", 3))  # "3234"
    print(solution("4177252841", 4))  # "775841"
    print(solution("4177252841", 9))  # "8"
    print(solution(''.join(['9' for _ in range(100)]), 100 - 1))  # "8"
    print(solution(''.join(['9' for _ in range(10000)]), 10000 - 1))  # "8"
    # print(solution("999999999", 8))  # "775841"
