class Solution:
    def compress(self, chars: List[str]) -> int:
        compressed = []
        while chars:
            c = chars.pop(0)
            compressed.append(c)

            cnt = 1
            while chars and chars[0] == c:
                cnt += 1
                chars.pop(0)

            if cnt == 1:
                continue

            compressed.extend(str(cnt))

        chars[:] = compressed
        return len(chars)
