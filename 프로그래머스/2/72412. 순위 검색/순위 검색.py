from itertools import combinations
from collections import defaultdict
from bisect import bisect_left


def solution(information, queries):
    answer = []
    info_dict = defaultdict(list)

    for info in information:
        info = info.split()
        score = int(info.pop())
        for i in range(5):
            for c in combinations(info, i):
                info_dict[c].append(score)

    for info in info_dict.values():
        info.sort()

    for query in queries:
        query = query.replace(" and ", " ").split()
        query, query_score = (
            tuple(filter(lambda x: x != "-", query[:-1])),
            int(query[-1]),
        )

        answer.append(
            len(info_dict[query]) - bisect_left(info_dict[query], query_score)
        )

    return answer
