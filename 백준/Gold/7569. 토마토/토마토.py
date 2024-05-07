import sys
from collections import deque

input = sys.stdin.readline


def init(M, N, H):
    box = [[[] for _ in range(N)] for _ in range(H)]
    queue = deque()
    for z in range(H):
        for y in range(N):
            box[z][y][:] = list(map(int, input().split()))
            for x in range(M):
                if box[z][y][x] == 1:
                    queue.append([z, y, x])
    return box, queue


def check_box(box):
    ret = -1
    for floor in box:
        for row in floor:
            if 0 in row:
                return -1
            else:
                ret = max(ret, max(row))
    return ret - 1


def bfs(M, N, H):
    box, queue = init(M, N, H)
    dirs = (
        (1, 0, 0),
        (-1, 0, 0),
        (0, 1, 0),
        (0, -1, 0),
        (0, 0, 1),
        (0, 0, -1),
    )

    while queue:
        z, y, x = queue.popleft()

        for dz, dy, dx in dirs:
            nz, ny, nx = z + dz, y + dy, x + dx

            if not (0 <= nx < M and 0 <= ny < N and 0 <= nz < H):
                continue

            if box[nz][ny][nx] == 0:
                box[nz][ny][nx] = box[z][y][x] + 1
                queue.append((nz, ny, nx))

    return check_box(box)


if __name__ == "__main__":
    M, N, H = map(int, input().split())
    print(bfs(M, N, H))
