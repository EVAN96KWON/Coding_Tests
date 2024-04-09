def solution(n, results):
    answer = 0
    graph = dict()

    for rst in results:
        print(rst)
        if graph[rst[0]]:
            graph[rst[0]].append(rst[1])
        else:
            graph[rst[0]] = [rst[1]]

    for it in graph:
        print(it)

    return answer


if __name__ == '__main__':
    print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))
