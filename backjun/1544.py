N = int(input())
words = list(input() for _ in range(N))

for i in range(len(words)):
    current = words[i]
    for j in range(len(current)):
        cycle = current[j:] + current[:j]

        if cycle in words:
            words[words.index(cycle)] = words[i]

print(len(set(words)))