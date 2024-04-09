from string import ascii_uppercase


def solution(msg):
    index_dict = {ascii_uppercase[i]: i + 1 for i in range(26)}
    answer = []

    i = 0
    while i < len(msg):
        j = i + 1
        while j <= len(msg):
            if msg[i:j] not in index_dict:
                index_dict[msg[i:j]] = len(index_dict) + 1
                answer.append(index_dict[msg[i : j - 1]])
                i = j - 1
                break
            j += 1
        else:
            answer.append(index_dict[msg[i:j]])
            break

    return answer
