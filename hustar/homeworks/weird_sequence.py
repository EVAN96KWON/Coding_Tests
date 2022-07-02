def main():
    max_num = 1000000
    weird_seq = [1, 1] + [0] * max_num

    for i in range(2, max_num + 1):
        if i % 2 == 0:
            weird_seq[i] = (2 * weird_seq[i - 1] + weird_seq[i - 2]) % 20211209
        else:
            weird_seq[i] = (weird_seq[i - 1] + 2 * weird_seq[i - 2]) % 20211209

    for t in range(int(input())):
        print(weird_seq[int(input())])


if __name__ == '__main__':
    main()

'''
8
0
1
2
3
4
5
10000
1000000
'''