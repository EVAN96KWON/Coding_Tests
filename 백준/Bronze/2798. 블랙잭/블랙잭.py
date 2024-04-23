from itertools import combinations


def blackjack(n, target, cards):
    cur = -1
    for comb in combinations(cards, 3):
        if sum(comb) == target:
            return sum(comb)
        elif sum(comb) < target:
            cur = max(cur, sum(comb))
    return cur


if __name__ == "__main__":
    N, M = list(map(int, input().split()))
    cards = list(map(int, input().split()))
    print(blackjack(N, M, cards))
