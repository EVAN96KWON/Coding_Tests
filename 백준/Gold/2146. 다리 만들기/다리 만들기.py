from collections import deque
import sys

input = sys.stdin.readline


def search_islands(board):
    def bfs(x, y, mark):
        board[y][x] = mark
        queue = deque([(x, y)])
        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))

        while queue:
            x, y = queue.popleft()

            for dx, dy in dirs:
                nx, ny = x + dx, y + dy

                if not (0 <= nx < N and 0 <= ny < N):
                    continue

                if board[ny][nx] != 1:
                    continue

                queue.append((nx, ny))
                board[ny][nx] = mark

        return mark + 1

    mark = 2
    for x in range(N):
        for y in range(N):
            if board[y][x] != 1:
                continue

            mark = bfs(x, y, mark)
    return board


def bridge_islands(board):
    def bfs(x, y):
        visited = [[0] * N for _ in range(N)]
        queue = deque([(x, y)])
        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))

        id_island = board[y][x]

        while queue:
            x, y = queue.popleft()

            for dx, dy in dirs:
                nx, ny = x + dx, y + dy

                if not (0 <= nx < N and 0 <= ny < N):
                    continue

                if visited[ny][nx] or board[ny][nx] == id_island:
                    continue

                if board[ny][nx] != 0:
                    return visited[y][x]

                queue.append((nx, ny))
                visited[ny][nx] = visited[y][x] + 1

        return N * N

    ret = N * N
    for x in range(N):
        for y in range(N):
            if board[y][x] == 0:
                continue

            ret = min(ret, bfs(x, y))
    return ret


if __name__ == "__main__":
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    board = search_islands(board)
    answer = bridge_islands(board)
    print(answer)
