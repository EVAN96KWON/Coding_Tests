from functools import lru_cache


@lru_cache(maxsize=None)
def fibo(n: int):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)


def main():
    for TC in range(int(input())):
        print(fibo(int(input())))


if __name__ == '__main__':
    main()
