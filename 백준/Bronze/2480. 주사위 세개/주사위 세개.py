def result(nums):
    if nums[0] == nums[1] == nums[2]:
        return 10000 + nums[0] * 1000
    elif nums[0] == nums[1]:
        return 1000 + nums[0] * 100
    elif nums[0] == nums[2]:
        return 1000 + nums[0] * 100
    elif nums[1] == nums[2]:
        return 1000 + nums[1] * 100
    else:
        return max(nums) * 100


if __name__ == '__main__':
    num1, num2, num3 = map(int, input().split())
    arr = [num1, num2, num3]
    print(result(arr))