def mv(s):
    stack, cnt110, i = [], 0, 0

    # find and del "110", count del
    while i < len(s):
        stack.append(s[i])
        i += 1

        if stack[-3:] == ["1", "1", "0"]:
            cnt110 += 1
            del stack[-3:]

    # find "0" for append "011"
    # if not found, append at last
    stack = "".join(reversed(stack))  # reverse stack
    idx = stack.find("0")

    if idx >= 0:
        res = stack[:idx] + "011" * cnt110 + stack[idx:]
    else:
        res = stack + "011" * cnt110

    return "".join(reversed(res))


def solution(s):
    return list(map(mv, s))
