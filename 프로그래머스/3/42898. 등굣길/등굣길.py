def solution(m, n, puddles):
    roots = [[0 for _ in range(m)] for _ in range(n)]
    roots[0][0] = 1

    for y in range(n):
        for x in range(m):
            if x == 0 and y == 0:
                continue
            if [x + 1, y + 1] in puddles:
                continue

            roots[y][x] = (roots[y - 1][x] + roots[y][x - 1]) % 1_000_000_007

    return roots[-1][-1]
