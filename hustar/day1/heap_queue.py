import heapq


class HeapQueue:
    def __init__(self):
        self.heapq = list()

    def push(self, x):
        heapq.heappush(self.heapq, x)

    def pop(self):
        return heapq.heappop(self.heapq)


def main():
    for tc in range(int(input())):
        queue = HeapQueue()
        for n in range(int(input())):
            item = int(input())
            print(queue.pop()) if item == -1 else queue.push(item)


if __name__ == '__main__':
    main()
