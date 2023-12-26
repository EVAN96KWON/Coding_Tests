if __name__ == '__main__':
    M, N = map(int, input().split())
    nums_list = []
    num_dic = {"0": "zero", "1": "one", "2": "two", "3": "three", "4": "four",
               "5": "five", "6": "six", "7": "seven", "8": "eight", "9": "nine"}

    for i in range(M, N + 1):
        s = ' '.join([num_dic[c] for c in str(i)])
        nums_list.append([i, s])

    nums_list.sort(key=lambda x: x[1])

    for i in range(len(nums_list)):
        e = ' ' if (i + 1) % 10 else '\n'
        print(nums_list[i][0], end=e)

