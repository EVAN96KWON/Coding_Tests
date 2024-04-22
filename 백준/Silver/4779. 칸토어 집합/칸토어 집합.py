def cantorian(line: str) -> str:
    if len(line) == 1:
        return line
    
    s = len(line) // 3
    prefix = line[:s]
    postfix = line[-s:]
    
    return cantorian(prefix) + " " * s + cantorian(postfix)

while True:
    try:
        n = int(input())
        line = "-" * (3 ** n)
        print(cantorian(line))
    except:
        break