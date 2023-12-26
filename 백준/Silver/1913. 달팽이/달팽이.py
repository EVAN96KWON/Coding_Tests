def draw_snail():
    global N
    cnt = num = 2
    t = 0
    d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    snail[N // 2][N // 2] = 1
    x = y = N // 2 - 1

    while True:
        for _ in range(4):
            a, b = d[t % 4]
            for _ in range(cnt):
                x += a
                y += b
                snail[x][y] = num
                if num == look:
                    ans[0] = x + 1
                    ans[1] = y + 1
                if num == N ** 2:
                    return
                num += 1
            t += 1
        cnt += 2
        x -= 1
        y -= 1


if __name__ == '__main__':
    N = int(input())
    look = int(input())
    snail = [[0 for __ in range(N)] for _ in range(N)]
    ans = [N // 2 + 1, N // 2 + 1]
    draw_snail()
    for i in snail:
        print(*i)
    print(*ans)
