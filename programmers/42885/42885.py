def solution(people, limit):
    people.sort()
    boat = people[0]
    answer = 0

    for person in people[1:]:
        if boat + person <= limit:
            pass

    return answer + 1


if __name__ == '__main__':
    print(solution([70, 50, 80, 50], 100))  # 3
    print(solution([70, 80, 50], 100))  # 3
