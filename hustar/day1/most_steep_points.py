

def main():
    for TC in range(int(input())):
        points = [tuple(map(int, input().split())) for _ in range(int(input()))]
        points.sort(key=lambda x: x[0])
        print(points)
        x, y = 0, 1
        grads = []
        for p in range(len(points)):
            for q in range(p + 1, len(points)):
                grad = abs((points[p][y] - points[q][y]) / (points[p][x] - points[q][x]))
                grads.append([points[p], points[q], grad])

        print(grads)


if __name__ == '__main__':
    main()
