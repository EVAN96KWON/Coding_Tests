from collections import deque


class Queue:
    def __init__(self):
        self.stack = deque()

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        return self.stack.popleft()


def main():
    for tc in range(int(input())):
        queue = Queue()
        for n in range(int(input())):
            item = int(input())
            print(queue.pop()) if item == -1 else queue.push(item)


if __name__ == '__main__':
    main()
