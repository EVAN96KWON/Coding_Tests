from collections import defaultdict


def solution(weights):
    answer = 0
    weight_dict = defaultdict(float)
    ratios = [1 / 1, 1 / 2, 2 / 1, 2 / 3, 3 / 2, 3 / 4, 4 / 3]
    for weight in weights:
        for ratio in ratios:
            answer += weight_dict[weight * ratio]
        weight_dict[weight] += 1

    return int(answer)
