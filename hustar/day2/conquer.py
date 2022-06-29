from collections import deque


def main():
    for TC in range(int(input())):
        list1 = deque(map(int, input().split()))
        list2 = deque(map(int, input().split()))
        answer = deque()

        while list1 and list2:
            if list1[0] < list2[0]:
                answer.append(1)
                list1.popleft()
            else:
                answer.append(2)
                list2.popleft()

        if not list1:
            while list2:
                answer.append(2)
                list2.popleft()
        elif not list2:
            while list1:
                answer.append(1)
                list1.popleft()

        print(*answer)


if __name__ == '__main__':
    main()
