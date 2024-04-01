from typing import Tuple


def distance(point1: Tuple[int, int], point2: Tuple[int, int]) -> float:
    return (point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2


def min_dist(sp: Tuple[int, int], ep: Tuple[int, int], m: int, n: int):
    sx, sy = sp
    ex, ey = ep
    dist = float('inf')

    if not (sx == ex and sy > ey):
        dist = min(dist, distance((sx, -sy), (ex, ey)))

    if not (sx == ex and sy < ey):
        dist = min(dist, distance((sx, 2 * n - sy), (ex, ey)))

    if not (sy == ey and sx > ex):
        dist = min(dist, distance((-sx, sy), (ex, ey)))

    if not (sy == ey and sx < ex):
        dist = min(dist, distance((2 * m - sx, sy), (ex, ey)))

    return dist


def solution(m, n, startX, startY, balls):
    start_point = (startX, startY)
    return [min_dist(start_point, ball, m, n) for ball in balls]
