def solution(s, n):
    big_alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    small_alpha = "abcdefghijklmnopqrstuvwxyz"
    answer = ""

    for c in s:
        if c == " ":
            converted_c = " "
            answer += converted_c
            continue

        if c.isupper():
            idx = big_alpha.find(c)
            idx = (idx + n) % 26
            converted_c = big_alpha[idx]
            answer += converted_c
        else:
            idx = small_alpha.find(c)
            idx = (idx + n) % 26
            converted_c = small_alpha[idx]
            answer += converted_c

    return answer
