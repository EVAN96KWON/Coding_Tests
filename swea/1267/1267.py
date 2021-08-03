def my_cal(num1, num2, op):
    if op == '/':
        if num2 == '0':
            return False
        d, m = divmod(int(num1), int(num2))
        if m == 0:
            return int(d)
    return str(eval(num1 + op + num2))


def make_nums(nums, ops):
    tmp = list(nums.keys())

    return nums


def main():
    T = int(input())
    for test_case in range(1, T + 1):
        N, O, M = map(int, input().split())
        nums = dict()
        for x in input().split():
            nums[x] = 1
        ops = []
        for op in input().split():
            if op == '1':   ops.append('+')
            elif op == '2': ops.append('-')
            elif op == '3': ops.append('*')
            else:           ops.append('/')

        print(nums)
        print(ops)
        print(input("target -> "))


if __name__ == '__main__':
    num1 = input()
    num2 = input()
    op = input()
    print(my_cal(num1, num2, op))
    main()
