from itertools import combinations

if __name__ == "__main__":
    while _input := input():
        if _input == "0":
            break

        _, *nums = _input.split()
        for comb in combinations(nums, 6):
            print(" ".join(comb))
        print()
