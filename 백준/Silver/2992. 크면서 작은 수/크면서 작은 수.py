from itertools import permutations

if __name__ == '__main__':
    X = input()
    nums = [int(X)]

    for num in list(permutations(list(X), len(X))):
        int_num = int("".join(num))
        if int_num > int(X):
            nums.append(int_num)
    nums = sorted(nums)

    X_idx = nums.index(int(X))
    if X_idx + 1 >= len(nums):
        print(0)
    else:
        print(nums[X_idx + 1])
