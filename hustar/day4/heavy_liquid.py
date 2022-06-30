import math
from collections import deque


class Liquids:
    def __init__(self, liquids: list) -> None:
        # sort by W/V
        self.liquids = deque(
            sorted(liquids, key=lambda x: x[0]/x[1])
        )

    def get_heaviest_liquid(self, target_ml: int) -> int:
        liquids = self.liquids.copy()
        result_w = 0
        result_v = 0

        while result_v < target_ml:
            w, v = liquids.pop()
            if target_ml - result_v > v:
                result_w += w
                result_v += v
            else:
                result_w += w / v * min(target_ml - result_v, v)
                result_v += min(target_ml - result_v, v)

        return math.floor(result_w)


def main():
    for T in range(int(input())):
        N, C = map(int, input().split())
        liquids = Liquids([tuple(map(int, input().split())) for _ in range(N)])
        print(liquids.get_heaviest_liquid(C))


if __name__ == '__main__':
    main()

'''
2
4 100
100 30
50 30
200 40
120 55
5 340
795 953
41 206
524 422
985 574
135 932
'''