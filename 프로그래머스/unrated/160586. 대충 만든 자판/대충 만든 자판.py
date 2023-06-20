def solution(keymap, targets):
    answer = []
    _keymap = {}
    for key in keymap:
        for i, k in enumerate(key):
            if k in _keymap:
                _keymap[k] = min(_keymap[k], i)
            else:
                _keymap[k] = i

    for target in targets:
        cnt = 0
        for t in target:
            if t not in _keymap:
                cnt = -1
                break
            cnt += _keymap[t] + 1
        answer.append(cnt)

    return answer