def compress(s, n):
    sliced = [s[i:i+n] for i in range(0, len(s), n)]
    compressed = ""
    i = 0
    while i < len(sliced):
        cnt = 0
        for j in range(i, len(sliced)):
            if sliced[i] != sliced[j]:
                break
            cnt += 1
            i = j
        compressed += str(cnt) + sliced[i] if cnt != 1 else sliced[i]
        i += 1
    return compressed


def solution(s):
    compresses = [len(compress(s, i)) for i in range(1, len(s))]
    return min(compresses) if compresses else 1


if __name__ == '__main__':
    print(solution("aabbaccc"))  # 7
    print(solution("ababcdcdababcdcd"))  # 9
    print(solution("abcabcdede"))  # 8
    print(solution("abcabcabcabcdededededede"))  # 14
    print(solution("xababcdcdababcdcd"))  # 17
    print(solution("a"))  # 1
