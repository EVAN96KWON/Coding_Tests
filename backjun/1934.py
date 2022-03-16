import math

if __name__ == '__main__':
    T = int(input())
    answers = []

    for i in range(T):
        A, B = map(int, input().split())
        answers.append(math.lcm(A, B))

    for answer in answers:
        print(answer)
