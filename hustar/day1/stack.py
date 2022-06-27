from collections import deque


class Stack:
    def __init__(self):
        self.stack = deque()

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        return self.stack.pop()


def main():
    for tc in range(int(input())):
        stack = Stack()
        for n in range(int(input())):
            item = int(input())
            print(stack.pop()) if item == -1 else stack.push(item)


if __name__ == '__main__':
    main()
