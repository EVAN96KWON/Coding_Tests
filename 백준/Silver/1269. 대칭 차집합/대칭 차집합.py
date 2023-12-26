if __name__ == '__main__':
    len_A, len_B = input().split()
    A = set(map(int, input().split()))
    B = set(map(int, input().split()))
    print(len((A - B) | (B - A)))
