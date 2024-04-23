seq = []

if __name__ == "__main__":
    A = int(input())
    T = int(input())
    call = int(input())
    round = 0

    while len(seq) < T * 2:
        _extend = [0, 1, 0, 1] + [0] * (round + 2) + [1] * (round + 2)
        seq.extend(_extend)
        round += 1

    cnt = 0
    for i, cur in enumerate(seq):
        if cur == call:
            cnt += 1

        if cnt == T:
            break

    print(i % A)
