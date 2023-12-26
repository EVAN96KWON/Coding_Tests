def solution(phone_number):
    return "".join(['*' if i < len(phone_number) - 4 else phone_number[i] for i in range(len(phone_number))])


def solution2(phone_number):
    return '*' * (len(phone_number) - 4) + phone_number[-4:]


if __name__ == '__main__':
    print(solution("01033334444"))
    print(solution("027778888"))
