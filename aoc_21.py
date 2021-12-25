WINNING_SCORE = 1000

def hsdd():
    # 100-sided deterministic dice
    while True:
        for i in range(100):
            yield i + 1

class DeterministicGame:
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

            if self.score[side] >= WINNING_SCORE:
                break

            side = (side + 1) % 2

        print(f'Winner is player {side + 1} with score {self.score[side]}.')
        print(self.dice_rolls, 'dice rolls')

        side = (side + 1) % 2
        print('result=', self.dice_rolls * self.score[side])


if __name__ == '__main__':
    # part 1
    game = DeterministicGame(7, 2)
    game.play()

    # part 2
    pass
