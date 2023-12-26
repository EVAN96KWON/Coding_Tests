if __name__ == '__main__':
    T = int(input())
    answers = list()

    for i in range(T):
        A = sorted(list(map(int, input().split())))
        answers.append(A[7])

    for answer in answers:
        print(answer)
