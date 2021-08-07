def solution(n, a, b):
    answer = 0
    tournament = [str(i + 1) for i in range(n)]
    tournament[a - 1] = 'A'
    tournament[b - 1] = 'B'
    while tournament:
        n //= 2
        answer += 1
        where_A = tournament.index('A') // 2
        where_B = tournament.index('B') // 2

        if where_A == where_B:
            return answer

        next_tournament = [str(i + 1) for i in range(n)]
        next_tournament[where_A] = 'A'
        next_tournament[where_B] = 'B'
        tournament = next_tournament

    return answer


if __name__ == '__main__':
    print(solution(8, 4, 7))  # 3
    print(solution(8, 3, 4))  # 3
    print(solution(8, 1, 4))  # 3
