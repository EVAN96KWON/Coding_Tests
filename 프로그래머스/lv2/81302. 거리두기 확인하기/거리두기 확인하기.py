def find_person(place, distance, nx, ny):
    # check manhattan distance
    if not distance < 3:
        return True
    # check current pos
    if not 0 <= ny < len(place) or not 0 <= nx < len(place[ny]):
        return True
    # if partition, then return True
    # if Person, then return False
    if place[ny][nx] == 'X':
        return True
    elif place[ny][nx] == 'P':
        return False

    # go to right, down, left, up
    xs = [1, 0, -1, 0]
    ys = [0, 1, 0, -1]
    for i in range(4):
        dx = nx + xs[i]
        dy = ny + ys[i]
        if not find_person(place, distance + 1, dx, dy):
            return False

    return True


def is_safe(place):
    # check this place
    for y in range(len(place)):
        for x in range(len(place[y])):
            if place[y][x] == 'P':
                tmp = list(place[y])
                tmp[x] = 'N'
                place[y] = ''.join(tmp)
                if not find_person(place, 0, x, y):
                    return False
    return True


def solution(places):
    answer = []
    for place in places:
        answer.append(1) if is_safe(place) else answer.append(0)
    return answer


if __name__ == '__main__':
    print(solution(
        [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
         ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
         ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
         ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
         ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
    ))
