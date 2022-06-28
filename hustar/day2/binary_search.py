def binary_search(arr, k, start, end):
    if start > end:
        return -1

    mid = (start + end) // 2

    if arr[mid] == k:
        return mid
    elif arr[mid] > k:
        end = mid - 1
    else:
        start = mid + 1

    return binary_search(arr, k, start, end)


def main():
    for TC in range(int(input())):
        arr = list(map(int, input().split()))
        find = list(map(int, input().split()))
        print(*[binary_search(arr, f, 0, len(arr) - 1) for f in find])


if __name__ == '__main__':
    main()
