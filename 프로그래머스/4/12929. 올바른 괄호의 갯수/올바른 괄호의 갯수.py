CATALAN = [1]
for i in range(1, 15):
    CATALAN.append(sum(CATALAN[j] * CATALAN[i - j - 1] for j in range(i)))


def solution(n):
    return CATALAN[n]
