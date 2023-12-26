def solution(people, limit):
    answer = 0
    people.sort()
    i, j = 0, len(people) - 1
    while i <= j:
        answer += 1
        i += 1 if people[i] + people[j] <= limit else 0
        j -= 1
    return answer


if __name__ == '__main__':
    print(solution([70, 50, 80, 50], 100))  # 3
    print(solution([70, 80, 50], 100))  # 3
