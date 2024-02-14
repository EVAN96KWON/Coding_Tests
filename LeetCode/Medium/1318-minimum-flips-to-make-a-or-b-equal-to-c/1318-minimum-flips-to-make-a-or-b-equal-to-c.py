class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        flips = 0

        while a or b or c:
            bit_a = a & 1
            bit_b = b & 1
            bit_c = c & 1

            if not bit_a | bit_b == bit_c:
                flips += (bit_a + bit_b) if bit_c == 0 else 1

            a >>= 1
            b >>= 1
            c >>= 1

        return flips
