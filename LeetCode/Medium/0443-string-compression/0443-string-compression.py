from collections import deque


class Solution:
    def compress(self, chars: List[str]) -> int:
        stack = deque(chars)
        compressed = deque()
        while stack:
            c = stack.popleft()
            compressed.append(c)

            cnt = 1
            while stack and stack[0] == c:
                cnt += 1
                stack.popleft()

            if cnt == 1:
                continue

            compressed.extend(str(cnt))

        chars[:] = list(compressed)
        return len(chars)
