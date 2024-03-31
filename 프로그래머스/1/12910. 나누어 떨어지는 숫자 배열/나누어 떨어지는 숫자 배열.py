def solution(arr, divisor):
    return [n for n in sorted(arr) if n % divisor == 0] or [-1]

