import itertools


def init_my_dic():
    temp = list()
    for i in range(1, 6):
        temp += list(itertools.product(gathers, repeat=i))
    return sorted(temp)


gathers = ['A', 'E', 'I', 'O', 'U']
my_dic = init_my_dic()
solution = lambda word: my_dic.index(tuple(word)) + 1

if __name__ == '__main__':
    print(solution("AAAAE", ))  # 6
    print(solution("AAAE"))  # 10
    print(solution("I"))  # 1563
    print(solution("EIO"))  # 1189


# solution = lambda word: sorted(["".join(c) for i in range(5) for c in product("AEIOU", repeat=i+1)]).index(word) + 1