def solution(routes):
    if not routes:
        return 0

    routes.sort(key=lambda x: x[1])
    cctvs = 1
    cctvs_pos = routes[0][1]

    for s, e in routes:
        if s > cctvs_pos:
            cctvs += 1
            cctvs_pos = e

    return cctvs
