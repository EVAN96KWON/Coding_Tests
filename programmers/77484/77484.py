def solution1(lottos, win_nums):
    lst = [6, 6, 5, 4, 3, 2, 1]
    min = 0

    for i in lottos:
        if i in win_nums:
            min += 1

    return [lst[min + lottos.count(0)], lst[min]]


def solution(lottos, win_nums):
    rank = [6, 6, 5, 4, 3, 2, 1]
    len_correct = len(set(lottos) & set(win_nums))
    len_hidden = lottos.count(0)
    return [rank[len_hidden + len_correct], rank[len_correct]]


if __name__ == '__main__':
    print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))  # [3, 5]
    print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]))  # [1, 6]
    print(solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]))  # [1, 1]
