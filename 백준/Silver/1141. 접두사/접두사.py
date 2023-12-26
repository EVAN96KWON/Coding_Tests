import sys

if __name__ == '__main__':
    rm_list = list()
    N = int(sys.stdin.readline())
    words = sorted(
        list(set([sys.stdin.readline().strip() for _ in range(N)])),
        key=len,
        reverse=True)

    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if words[i].startswith(words[j]):
                rm_list.append(words[j])
    print(len(list(set(words) - set(rm_list))))
