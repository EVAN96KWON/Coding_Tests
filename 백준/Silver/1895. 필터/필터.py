if __name__ == '__main__':
    R, C = map(int, input().split())
    image = [list(map(int, input().split())) for _ in range(R)]
    T = int(input())
    cnt = 0

    for i in range(1, R - 1):
        for j in range(1, C - 1):
            if sorted([image[i + _][j + __] for _ in (-1, 0, 1) for __ in (-1, 0, 1)])[4] >= T:
                cnt += 1

    print(cnt)
