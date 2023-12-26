def solution(info, query):
    answer = []
    _infoes = [_.split() for _ in info]
    _queries = [[__[0], __[2], __[4], __[6], __[7]] for __ in [_.split() for _ in query]]

    cnt = 0
    for _query in _queries:
        print(f'--> {_query}')
        for _info in _infoes:
            is_ok = True
            print(f'--> {_info}')
            for q, i in zip(_query, _info):
                if q == '-':
                    continue

                if q.isdecimal() and i.isdecimal():
                    if int(q) > int(i):
                        is_ok = False
                        break
                elif q != i:
                    is_ok = False
                    break

                print(f'{q} and {i}, {is_ok}')
            cnt += 1 if is_ok else 0
        print(cnt)
    return answer


if __name__ == '__main__':
    print(solution(
        ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
         "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"],
        ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
         "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100",
         "- and - and - and - 150"]))
