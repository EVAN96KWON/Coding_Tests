def solution(number, k):
    stack = [number[0]]

    # 숫자 순회
    for i in range(1, len(number)):
        # 스택이 비지 않은 동안, k >0 일때 동안, 스택의 제일 끝이 i번째 수보다 작을 때
        while stack and k > 0 and stack[-1] < number[i]:
            k -= 1
            stack.pop()
        # 스택에 i번째 수 추가
        stack.append(number[i])

    # 만약 k가 0이 아니라면, 남은 부분은 삭제
    stack = stack[:-k] if k != 0 else stack

    return ''.join(stack)


if __name__ == '__main__':
    print(solution("1924", 2))  # "94"
    print(solution("1231234", 3))  # "3234"
    print(solution("4177252841", 4))  # "775841"
