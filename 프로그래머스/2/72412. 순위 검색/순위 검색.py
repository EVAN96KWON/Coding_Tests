from itertools import combinations
from collections import defaultdict
from bisect import bisect_left, insort


def solution(information, queries):
    answer = []
    info_dict = defaultdict(list)

    for info in information:
        info = info.split()
        score = int(info.pop())
        for i in range(5):
            for c in combinations(info, i):
                insort(info_dict[c], score)

    for query in queries:
        query = query.replace(" and ", " ").replace("-", "").split()
        query, query_score = tuple(query[:-1]), int(query[-1])
        answer.append(
            len(info_dict[query]) - bisect_left(info_dict[query], query_score)
        )

    return answer
