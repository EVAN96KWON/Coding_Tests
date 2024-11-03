class Player:
    def __init__(self, video_len, pos, op_start, op_end, commands):
        self.video_len = self.__mmss2s__(video_len)
        self.pos = self.__mmss2s__(pos)
        self.op = (self.__mmss2s__(op_start), self.__mmss2s__(op_end))
        self.commands = commands

    @staticmethod
    def __mmss2s__(mmss: str) -> int:
        _mmss = mmss.split(":")
        return int(_mmss[0]) * 60 + int(_mmss[1])

    @staticmethod
    def __s2mmss__(s: int) -> str:
        return f"{s // 60:02}:{s % 60:02}"

    def do_command(self) -> str:
        for command in self.commands:
            self.skip_op()
            if command == "next":
                self.do_next()
            elif command == "prev":
                self.do_prev()
        self.skip_op()
        return self.__s2mmss__(self.pos)

    def do_next(self) -> None:
        self.pos = min(self.pos + 10, self.video_len)

    def do_prev(self) -> None:
        self.pos = max(self.pos - 10, 0)

    def skip_op(self) -> None:
        if self.pos in range(*self.op):
            self.pos = self.op[1]


def solution(video_len, pos, op_start, op_end, commands):
    player = Player(video_len, pos, op_start, op_end, commands)
    answer = player.do_command()
    return answer
