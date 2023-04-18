def solution(price, money, count):
    rst = price * (count + 1) * (count / 2) - money
    return rst if rst >= 0 else 0


if __name__ == '__main__':
    print(solution(3, 20, 4))  # 10
    print(solution(3, 20, 5))  # 10
