def is_correct(brackets):
    stack = []

    for item in brackets:
        if item == '(' or item == '{' or item == '[':
            stack.append(item)
        else:
            if len(stack) == 0:
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

    return True if len(stack) == 0 else False


def solution(s):
    answer = 0
    for i in range(len(s)):
        answer += 1 if is_correct(s[i:] + s[:i]) else 0
    return answer


if __name__ == '__main__':
    print(solution("[](){}"))
    print(solution("}]()[{"))
    print(solution("[)(]"))
    print(solution("}}}"))
