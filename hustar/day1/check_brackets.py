from collections import deque


def is_correct(brackets):
    stack = deque()

    for item in brackets:
        if item == '(' or item == '{' or item == '[':
            stack.append(item)
        else:
            if not stack:
                stack.append(item)
            else:
                if item == ')' and stack[-1] == '(':
                    del stack[-1]
                elif item == '}' and stack[-1] == '{':
                    del stack[-1]
                elif item == ']' and stack[-1] == '[':
                    del stack[-1]
                else:
                    stack.append(item)

    return False if stack else True


def main():
    for TC in range(int(input())):
        print('YES') if is_correct(input()) else print('NO')


if __name__ == '__main__':
    main()
