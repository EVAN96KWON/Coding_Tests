from itertools import permutations


def is_prime(number):
    if number < 2:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True


def solution(numbers):
    answer = 0
    number_set = set()

    # make all possible numbers
    for i in range(len(numbers)):
        for item in list(permutations(numbers, i + 1)):
            number_set.add(int(''.join(item)))

    # check numbers is prime
    for it in number_set:
        answer += 1 if is_prime(it) else 0

    return answer


if __name__ == '__main__':
    print(solution("17"))  # 3
    print(solution("011"))  # 2
