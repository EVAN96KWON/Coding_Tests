def is_correct(v):
    for i in range(len(v)):
        if i == 0:
            if v[i] == '_' or v[i].isupper():
                return False
        else:
            if v[i - 1] == '_':
                if v[i] == '_':
                    return False
                if v[i].isupper():
                    return False
            if i == len(v) - 1:
                if v[i] == '_':
                    return False
        if v[i].isupper():
            if '_' in v:
                return False
    return True


def convert(v):
    result = ""
    if v.islower():             # cpp
        for i in range(len(v)):
            if v[i] == '_':
                continue

            if v[i - 1] == '_':
                result += v[i].upper()
            else:
                result += v[i]
    else:                       # java
        for i in range(len(v)):
            if v[i].isupper():
                result += '_' + v[i].lower()
            else:
                result += v[i]
    return result


if __name__ == '__main__':
    variable = input()
    if is_correct(variable):
        print(convert(variable))
    else:
        print('Error!')
