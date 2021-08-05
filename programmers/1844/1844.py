def bfs(maps, x, y, n, m):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = list()
    queue.append((x, y))

    while queue:
        x, y = queue.pop(0)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx not in range(0, n) or ny not in range(0, m):
                continue

            if maps[ny][nx] == 0:
                continue

            if maps[ny][nx] == 1:
                maps[ny][nx] = maps[y][x] + 1
                queue.append((nx, ny))

    return maps[m - 1][n - 1]


def solution(maps):
    answer = bfs(maps, 0, 0, len(maps[0]), len(maps))
    return answer if answer != 1 else -1


if __name__ == '__main__':
    print(solution([[1, 0, 1, 1, 1],
                    [1, 0, 1, 0, 1],
                    [1, 0, 1, 1, 1],
                    [1, 1, 1, 0, 1],
                    [0, 0, 0, 0, 1]]))  # 11

    print(solution([[1, 0, 1, 1, 1],
                    [1, 0, 1, 0, 1],
                    [1, 0, 1, 1, 1],
                    [1, 1, 1, 0, 0],
                    [0, 0, 0, 0, 1]]))  # -1

    print(solution([[1, 0, 1, 1, 1],
                    [1, 0, 1, 0, 1],
                    [1, 0, 1, 0, 1],
                    [1, 1, 1, 0, 1],
                    [0, 0, 0, 0, 1]]))  # -1
