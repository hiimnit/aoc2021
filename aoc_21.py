def hsdd():
    # 100-sided deterministic dice
    while True:
        for i in range(100):
            yield i + 1

class DeterministicGame:
    WINNING_SCORE = 1000

    def __init__(self, p1: int, p2: int) -> None:
        self.pos = [p1 - 1, p2 - 1]
        self.dice = hsdd()
        self.score = [0, 0]
        self.dice_rolls = 0

    def play(self):
        side = 0
        while True:
            rolls = next(self.dice) + next(self.dice) + next(self.dice)
            self.dice_rolls += 3
            self.pos[side] = (self.pos[side] + rolls) % 10
            self.score[side] += self.pos[side] + 1

            if self.score[side] >= DeterministicGame.WINNING_SCORE:
                break

            side = (side + 1) % 2

        print(f'Winner is player {side + 1} with score {self.score[side]} in {self.dice_rolls} dice rolls.')

        side = (side + 1) % 2
        print('result=', self.dice_rolls * self.score[side])

class DiracGame:
    WINNING_SCORE = 21
    # sums of all possible rolls
    ROLLS = [3,4,5,4,5,6,5,6,7,4,5,6,5,6,7,6,7,8,5,6,7,6,7,8,7,8,9]

    def __init__(self, p1: int, p2: int, mem: dict[str, tuple[int, int]],
                 s1: int = 0, s2: int = 0, side: int = 0, parent: 'DiracGame' = None) -> None:
        self.pos = [p1, p2]
        self.score = [s1, s2]
        self.side = side
        self.mem = mem
        self.result = [0, 0]
        
        self.parent = parent
        self.mem_counter = 0

    def play(self):
        games = [self]
        while games:
            game = games.pop()
            state = game.serialize_state()
            if state in self.mem:
                game.update_mem(self.mem[state], 27)
                continue

            for roll in DiracGame.ROLLS:
                copy = game.copy()
                copy.add(roll)
                if not copy.check_win():
                    copy.toggle_side()
                    games.append(copy)

        return self.result

    def add(self, roll: int):
        self.pos[self.side] = (self.pos[self.side] + roll) % 10
        self.score[self.side] += self.pos[self.side] + 1

    def check_win(self):
        win = self.score[self.side] >= DiracGame.WINNING_SCORE
        if win and self.parent:
            self.parent.update_mem([1,0] if self.side == 0 else [0,1])
        return win

    def update_mem(self, result: list[int], mem_counter: int = 1):
        self.mem_counter += mem_counter
        self.result[0] += result[0]
        self.result[1] += result[1]

        if self.mem_counter == 27:
            self.mem[self.serialize_state()] = tuple(self.result)
            if self.parent:
                self.parent.update_mem(self.result)

    def toggle_side(self):
        self.side = (self.side + 1) % 2

    def copy(self):
        return DiracGame(
            self.pos[0],
            self.pos[1],
            self.mem,
            self.score[0],
            self.score[1],
            self.side,
            parent=self,
        )

    def serialize_state(self):
        return f'{self.pos[0] + 1}-{self.pos[1] + 1}-{self.score[0]}-{self.score[1]}-{self.side}'


if __name__ == '__main__':
    # part 1
    game = DeterministicGame(7, 2)
    game.play()

    # part 2
    game = DiracGame(7 - 1, 2 - 1, {})
    print('result=', game.play())

