def solution(number, k):
    stack = [number[0]]

    for i in range(1, len(number)):
        while stack and stack[-1] < number[i] and k > 0:
            k -= 1
            stack.pop()
        stack.append(number[i])

    stack = stack[:-k] if k != 0 else stack

    return ''.join(stack)


if __name__ == '__main__':
    print(solution("1924", 2))  # "94"
    print(solution("1231234", 3))  # "3234"
    print(solution("4177252841", 4))  # "775841"
