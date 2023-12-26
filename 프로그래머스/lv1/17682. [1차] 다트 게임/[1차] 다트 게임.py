def split_tries(dartResult):
    tries = []
    for i in range(len(dartResult)):
        if dartResult[i].isnumeric():
            current_try = dartResult[i]
            for j in range(i + 1, len(dartResult)):
                if dartResult[j].isnumeric():
                    break
                current_try += dartResult[j]
            tries.append(current_try)

    for i in range(3):
        if len(tries[i]) == 1:
            tries[i] += tries[i + 1]
            del tries[i + 1]
    return tries


def get_point(tries):
    all_point = ''
    for t in tries:
        point = ''
        for i in range(0, len(t)):
            if t[i] == 'D':
                point = point + ' ** 2'
            elif t[i] == 'T':
                point = point + ' ** 3'
            elif t[i] == 'S':
                point = point
            elif t[i].isnumeric and t[i] != '*':
                point = point + t[i]
        if '#' in t:
            point = ' -1 * (' + point + ')'
        elif '*' in t:
            all_point = '(' + all_point + ' + (' + point + ')' + ') * 2'
        else:
            all_point += ' + (' + point + ')'
    return all_point


def solution(dartResult):
    tries = split_tries(dartResult)
    print(tries)
    all_point = ""
    print(get_point(tries))
    print(eval(get_point(tries)))

    return dartResult


if __name__ == '__main__':
    print(solution('1S2D*3T'))
    print(solution('1D2S#10S'))
    print(solution('1D2S0T'))
    print(solution('1S*2T*3S'))
    print(solution('1D#2S*3S'))
    print(solution('1T2D3D#'))
    print(solution('1D2S3T*'))
