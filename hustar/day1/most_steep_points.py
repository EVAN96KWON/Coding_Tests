import time


def main():
    for TC in range(int(input())):
        start = time.time()
        points = [tuple(map(int, input().split())) for _ in range(int(input()))]
        max_grad = 0
        max_points = []
        for p in range(len(points)):
            px, py = points[p]
            for q in range(p + 1, len(points)):
                qx, qy = points[q]

                grad = abs((py - qy) / (px - qx))

                if grad > max_grad:
                    max_grad = grad
                    max_points = [px, py, qx, qy] if px < qx else [qx, qy, px, py]
        print(" ".join(map(str, max_points)))
    end = time.time()
    print(format(end-start))


if __name__ == '__main__':
    main()
