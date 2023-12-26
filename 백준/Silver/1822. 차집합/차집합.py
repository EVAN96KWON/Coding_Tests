lenA, lenB = map(int, input().split())
A = set(map(int, input().split(" ")))
B = set(map(int, input().split(" ")))
C = list(map(str, sorted(A - B)))
print(len(C))
if len(C) >= 0:
    print(" ".join(C))
else:
    pass

