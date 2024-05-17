import sys

input = sys.stdin.readline

def search(dwarves):
    for i in range(9):
        for j in range(i + 1, 9):
            if dwarves[i] + dwarves[j] == diff:
                return dwarves[i], dwarves[j]
    return -1, -1
    

if __name__ == "__main__":
    dwarves = [int(input()) for _ in range(9)]
    diff = sum(dwarves) - 100
    fakes = search(dwarves)
    
    for dwarf in sorted(dwarves):
        if dwarf in fakes:
            continue
        
        print(dwarf)
