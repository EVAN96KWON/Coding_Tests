def solution(arr, divisor):
    ret = list(filter(lambda x: x % divisor == 0, arr))
    return [-1] if not ret else sorted(ret)
