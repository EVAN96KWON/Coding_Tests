import heapq


def solution(operations):
    answer = []
    for op in operations:
        IO, num = op.split(" ")
        if IO == "I":
            heapq.heappush(answer, int(num))
        else:
            if answer:
                if num.startswith("-"):
                    heapq.heappop(answer)
                else:
                    answer = heapq.nlargest(len(answer), answer)[1:]
                    heapq.heapify(answer)

    return [max(answer), min(answer)] if answer else [0, 0]


if __name__ == '__main__':
    print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))
    print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))
