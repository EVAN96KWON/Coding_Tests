def solution(N, road, K):
    answer = 0
    graph = {n: [] for n in range(N)}

    for r in road:
        graph[r[0] - 1].append(r[1] - 1)
        graph[r[1] - 1].append(r[0] - 1)

    return answer


if __name__ == '__main__':
    print(solution(5, [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]], 3))  # 4
    print(solution(6, [[1, 2, 1], [1, 3, 2], [2, 3, 2], [3, 4, 3], [3, 5, 2], [3, 5, 3], [5, 6, 1]], 4))  # 4
