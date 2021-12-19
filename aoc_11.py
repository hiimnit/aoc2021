input = [
    [2,6,8,2,5,5,1,6,5,1,],
    [3,2,2,3,1,3,4,2,6,3,],
    [5,8,4,8,4,7,1,4,1,2,],
    [7,4,3,8,3,3,4,8,6,2,],
    [8,7,3,1,3,2,1,5,7,3,],
    [6,4,1,5,2,3,3,5,7,4,],
    [5,5,6,4,7,2,6,8,4,3,],
    [6,6,8,3,4,5,6,4,4,5,],
    [8,5,8,2,3,4,6,1,1,2,],
    [4,6,1,7,5,8,8,2,3,6,],
]

def inc_guarded(octs: list[list[int]], i: int, j: int, energized: set, flashed: set):
    if i > 9 or i < 0 or j > 9 or j < 0:
        return
    
    octs[i][j] += 1

    if octs[i][j] > 9 and not (i, j) in flashed:
        energized.add((i, j))

def inc(octs: list[list[int]], i: int, j: int, energized: set, flashed: set):
    inc_guarded(octs, i - 1, j - 1, energized, flashed)
    inc_guarded(octs, i - 1, j, energized, flashed)
    inc_guarded(octs, i - 1, j + 1, energized, flashed)
    inc_guarded(octs, i, j - 1, energized, flashed)
    inc_guarded(octs, i, j + 1, energized, flashed)
    inc_guarded(octs, i + 1, j - 1, energized, flashed)
    inc_guarded(octs, i + 1, j, energized, flashed)
    inc_guarded(octs, i + 1, j + 1, energized, flashed)

def pretty_print(octs: list[list[int]]):
    for line in octs:
        print(''.join(str(o) for o in line))

if __name__ == '__main__':
    # part 1
    flashes = 0
    
    for _ in range(100):
        energized = set()
        flashed = set()
        for i, line in enumerate(input):
            for j, octopus in enumerate(line):
                input[i][j] += 1
                if input[i][j] > 9:
                    energized.add((i, j))
                    flashed.add((i, j))

        while len(energized) > 0:
            i, j = energized.pop()
            inc(input, i, j, energized, flashed)
            flashed.add((i, j))

        for i, line in enumerate(input):
            for j, octopus in enumerate(line):
                if input[i][j] > 9:
                    input[i][j] = 0
                    flashes += 1

    print('flashes=', flashes)

    # part 2
    for step in range(1000):
        energized = set()
        flashed = set()
        for i, line in enumerate(input):
            for j, octopus in enumerate(line):
                input[i][j] += 1
                if input[i][j] > 9:
                    energized.add((i, j))
                    flashed.add((i, j))

        while len(energized) > 0:
            i, j = energized.pop()
            inc(input, i, j, energized, flashed)
            flashed.add((i, j))

        for i, line in enumerate(input):
            for j, octopus in enumerate(line):
                if input[i][j] > 9:
                    input[i][j] = 0
                    flashed.add((i, j))

        if len(flashed) == 100:
            # add 100 steps performed in part 1
            print('result=', step + 1 + 100)
            break
