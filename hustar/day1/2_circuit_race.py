from collections import deque


def main():
    for TC in range(int(input())):
        queue = deque()

        for car in list(map(int, input().split())):
            if car not in queue:
                queue.append(car)
            else:
                if queue[0] == car:
                    queue.popleft()

        print(queue)
        print('YES') if queue else print('NO')


if __name__ == '__main__':
    main()
