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
                else:
                    break

        print('YES') if queue else print('NO')


if __name__ == '__main__':
    main()

'''
5
2
7 3 5 7 3 5
2
11 2 2 11
3
3 2 1 3 3 2 4 2 1 4 4 1
3
1 2 1 5 1 2 2 3 5 5 4 3 4 3 4
4
1 2 1 2 3 4 3 4 1 3 2 4 1 2 3 4
'''