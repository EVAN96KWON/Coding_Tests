from typing import List, Tuple


def get_start(board: List[str]) -> Tuple[int, int]:
    r, c = 0, 0
    for i, row in enumerate(board):
        if 'R' in row:
            r = i
            c = row.index('R')
            return r, c
    return (-1, -1)


def solution(board: List[str]) -> int:
    sr, sc = get_start(board)
    visited: List[Tuple[int, int]] = []
    queue: List[Tuple[int, int, int]] = [(sr, sc, 0)]

    while queue:
        cr, cc, step = queue.pop(0)

        if board[cr][cc] == 'G':
            return step

        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = cr, cc

            while (
                0 <= nr + dr < len(board)
                and 0 <= nc + dc < len(board[0])
                and board[nr + dr][nc + dc] != 'D'
            ):
                nr, nc = nr + dr, nc + dc

            if (nr, nc) not in visited:
                visited.append((nr, nc))
                queue.append((nr, nc, step + 1))

    return -1
