class ScoreBoard:
    def __init__(self, _map):
        self.scores = [_[:] for _ in _map]
        self.min_loss = 1000000

    def make_score_board(self):
        # make first row
        for i in range(1, len(self.scores)):
            self.scores[i][0] = self.scores[i][0] + self.scores[i - 1][0]
        # make first col
        for i in range(1, len(self.scores[0])):
            self.scores[0][i] = self.scores[0][i] + self.scores[0][i - 1]
        # make (1,1) to (m, n)
        for i in range(1, len(self.scores)):
            for j in range(1, len(self.scores[0])):
                self.scores[i][j] += min(self.scores[i - 1][j],
                                         self.scores[i][j - 1],
                                         self.scores[i - 1][j - 1])

        self.min_loss = self.scores[-1][-1]


def main():
    for t in range(int(input())):
        n, m = map(int, input().split())
        _map = [list(map(int, input().split())) for _ in range(n)]
        sb = ScoreBoard(_map)
        sb.make_score_board()
        print(sb.min_loss)


if __name__ == '__main__':
    main()

'''
2
3 4
4 0 0 0
0 2 3 4
1 3 5 2
3 5
1 1 2 1 1
1 2 1 2 1
1 1 1 1 1
'''
