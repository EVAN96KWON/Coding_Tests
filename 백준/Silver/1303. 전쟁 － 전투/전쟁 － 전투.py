def dfs(i, j, field, visited):
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    stack = [(i, j)]
    color = field[i][j]
    visited[i][j] = True
    count = 1

    while stack:
        i, j = stack.pop()
        for di, dj in dirs:
            ni, nj = i + di, j + dj
            if (
                0 <= ni < len(field) 
                and 0 <= nj < len(field[0]) 
                and not visited[ni][nj] 
                and field[ni][nj] == color
            ):
                stack.append((ni, nj))
                visited[ni][nj] = True
                count += 1

    return count


def main():
    N, M = map(int, input().split())
    field = [list(input()) for _ in range(M)]
    visited = [[False for _ in range(N)] for _ in range(M)]
    count = {"B": 0, "W": 0}

    for i in range(M):
        for j in range(N):
            if visited[i][j]:
                continue
            count[field[i][j]] += dfs(i, j, field, visited) ** 2

    print(count["W"], count["B"])


if __name__ == "__main__":
    main()
