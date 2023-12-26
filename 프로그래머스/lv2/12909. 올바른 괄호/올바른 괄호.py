from collections import deque


def solution(s):
    s, buf = deque(s), deque()

    while s:
        cur = s.popleft()
        if cur == ')':
            if not buf:         # buf is empty
                return False

            buf.pop() if buf[-1] == '(' else buf.append(cur)
        else:
            buf.append(cur)

    return True if not buf else False


if __name__ == '__main__':
    print(solution("()()"))  # true
    print(solution("(())()"))  # true
    print(solution(")()("))  # false
    print(solution("(()("))  # false
