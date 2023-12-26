from collections import deque


def bfs(graph, a, b, N, M):
    queue = deque()
    queue.append((a, b))
    graph[a][b] = 0

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
    return


if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        M, N, K = map(int, input().split())
        baechu = [tuple(map(int, input().split())) for _ in range(K)]
        bat = [[0 if (x, y) not in baechu else 1 for x in range(M)] for y in range(N)]

        cnt = 0
        for a in range(N):
            for b in range(M):
                if bat[a][b] == 1:
                    bfs(bat, a, b, N, M)
                    cnt += 1
        print(cnt)
