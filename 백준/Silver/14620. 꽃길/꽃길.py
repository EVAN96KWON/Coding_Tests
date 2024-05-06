import sys
from itertools import product, combinations

input = sys.stdin.readline
MAX = 10000000


def is_possible(seeds, N):
    _map = [[False] * N for _ in range(N)]
    _budget = 0
    dirs = ((0, 0), (1, 0), (-1, 0), (0, 1), (0, -1))

    def flowering(x, y):
        for dx, dy in dirs:
            if _map[x + dx][y + dy]:
                return False
        for dx, dy in dirs:
            _map[x + dx][y + dy] = True
        return True

    for seed in seeds:
        if flowering(*seed):
            for dx, dy in dirs:
                x, y = seed[0] + dx, seed[1] + dy
                _budget += hwadan[x][y]
        else:
            return MAX

    return _budget


if __name__ == "__main__":
    N = int(input())
    budget = MAX
    hwadan = [list(map(int, input().split())) for _ in range(N)]
    positions = product(range(1, N - 1), repeat=2)
    for seeds in combinations(positions, 3):
        budget = min(budget, is_possible(seeds, N))
    print(budget)
