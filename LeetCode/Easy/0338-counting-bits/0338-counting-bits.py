bits_cnt = [0]


class Solution:
    def countBits(self, n: int) -> List[int]:
        for i in range(len(bits_cnt), n + 1):
            bits_cnt.append(bits_cnt[i // 2] + i % 2)
        return bits_cnt[: n + 1]
