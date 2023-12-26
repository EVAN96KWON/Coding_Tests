def impact_mine(n):
    field[n] = True

    cur = n
    left = cur - 1
    while left >= 0 and mines[left] < mines[cur] and not field[left]:
        field[left] = True
        cur -= 1
        left -= 1

    cur = n
    right = cur + 1
    while right < len(mines) and mines[right] < mines[cur] and not field[right]:
        field[right] = True
        cur += 1
        right += 1


def print_field():
    print('====================================')
    for m in mines:
        print(m, end='\t')
    print()
    for f in field:
        if f:
            print('X', end='\t')
        else:
            print('_', end='\t')
    print()
    print('====================================')
    print()


def get_target():
    t = (mines[0], 0)  # (P, idx)

    for i in range(len(mines)):
        if not field[i]:
            if mines[i] > t[0]:
                t = (mines[i], i)

    return t[1]


if __name__ == '__main__':
    N = int(input())
    mines = [int(input()) for _ in range(N)]
    field = [False] * N
    targets = []

    print(mines)
    for i in range(N - 1):
        if i == N - 1 and mines[i - 1] <= mines[i]:
            print(i + 1)
        elif mines[i] >= mines[i + 1]:
            print(i + 1)
            j = i
            for j in range(i, N - 1):
                if mines[j] <= mines[j + 1]:
                    break
            i = j
