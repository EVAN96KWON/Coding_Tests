def solution(sequence, k):
    start, end = 0, 0
    sum = 0
    min_len = len(sequence)
    min_start = 0
    while start < len(sequence):
        if sum < k and end < len(sequence):
            sum += sequence[end]
            end += 1
        else:
            sum -= sequence[start]
            start += 1
        if sum == k:
            if end - start < min_len:
                min_len = end - start
                min_start = start
    return [min_start, min_start + min_len - 1]
