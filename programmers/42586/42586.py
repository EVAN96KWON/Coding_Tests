def solution(progresses, speeds):
    answer = []
    count = 0

    while progresses and speeds:
        if progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count != 0:
                answer.append(count)
                count = 0

            for i in range(len(progresses)):
                progresses[i] += speeds[i]

    return answer + [count]


if __name__ == '__main__':
    print(solution([93, 30, 55], [1, 30, 5]))  # [2, 1]
    print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))  # [1, 3, 2]
