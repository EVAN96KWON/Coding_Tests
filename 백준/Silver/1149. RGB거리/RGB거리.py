def main():
    N = int(input())
    tasks = [list(map(int, input().split())) for _ in range(N)]

    for i in range(1, N):
        for j in range(3):
            tasks[i][j] += min(tasks[i - 1][:j] + tasks[i - 1][j + 1 :])

    print(min(tasks[-1]))


if __name__ == "__main__":
    main()
