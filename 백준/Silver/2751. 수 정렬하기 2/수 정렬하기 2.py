import sys


def merge_sort(nums):
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    return merge(left, right)


def merge(left, right):
    merged = []
    left_idx, right_idx = 0, 0
    while left_idx < len(left) and right_idx < len(right):
        l, r = left[left_idx], right[right_idx]
        if l <= r:
            merged.append(l)
            left_idx += 1
        else:
            merged.append(r)
            right_idx += 1
    if left_idx < len(left):
        merged.extend(left[left_idx:])
    if right_idx < len(right):
        merged.extend(right[right_idx:])
    return merged


def main():
    N = int(sys.stdin.readline())
    nums = merge_sort([int(sys.stdin.readline()) for _ in range(N)])
    for n in nums:
        print(n)


if __name__ == "__main__":
    main()
