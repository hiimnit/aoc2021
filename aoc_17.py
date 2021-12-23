from math import sqrt, floor, ceil

input = 'target area: x=111..161, y=-154..-101'
input = [(111, 161), (-101, -154)]

# test input
# input = 'target area: x=20..30, y=-10..-5'
# input = [(20, 30), (-5, -10)]


# sum = (n + 1) * n / 2
# 2 * sum = n**2 + x * n
# 0 = n**2 + x * n - 2 * sum

# D = b**2 - 4 * a * c
# D = x**2 + 8 * sum

# n1 = (-1 - sqrt(D)) / 2
# n2 = (-1 + sqrt(D)) / 2

# -------------------------------

# sum = (s + s - n + 1) * n / 2
# 2 * sum = (2 * s - n + 1) * n
# 2 * sum = 2 * s * n - n * n + n
# 0 = n * n - 2 * s * n - n + 2 * sum
# 0 = n * n - (2 * s + 1) * n + 2 * sum

# D = 4 * s * s + 4 * s + 1 - 8 * sum

# n1 = (2 * s - 1 - sqrt(D)) / 2
# n2 = (2 * s - 1 + sqrt(D)) / 2

# -------------------------------

# sum = (s + s + n - 1) * n / 2
# 2 * sum = (2 * s + n - 1) * n
# 2 * sum = 2 * s * n + n * n - n
# 0 = n * n + 2 * s * n - n - 2 * sum
# 0 = n * n + (2 * s - 1) * n - 2 * sum

# D = 4 * s * s - 4 * s + 1 + 8 * sum

# n1 = (-2 * s + 1 - sqrt(D)) / 2
# n2 = (-2 * s + 1 + sqrt(D)) / 2

def solve(s: int):
    return (-1 + sqrt(1 + 8 * s)) * .5

def solve_y_w_start(sum: int, start:int):
    D = 4 * start * start - 4 * start + 1 + 8 * sum
    return (-2 * start + 1 + sqrt(D)) * .5

def solve_x_w_start(sum: int, start:int):
    D = 4 * start * start + 4 * start + 1 - 8 * sum
    if D < 0:
        return None
    return (2 * start - 1 - sqrt(D)) * .5

def linear_sum(n: int) -> int:
    return (n + 1) * n / 2

def calc_max_height(y: int, target_min: int, target_max: int):
    max_y = 0

    if y >= 0:
        max_y = linear_sum(y)
        target_min = max_y - target_min
        target_max = max_y - target_max
        n1 = ceil(solve(target_min)) + 1 + y
        n2 = floor(solve(target_max)) + 1 + y
    else:
        target_min = -target_min
        target_max = -target_max
        y = -y
        n1 = ceil(solve_y_w_start(target_min, y))
        n2 = floor(solve_y_w_start(target_max, y))

    solvable = n1 <= n2

    return max_y, solvable, n1, n2

def calc_x_solvable(x: int, target_min: int, target_max: int):
    n1 = solve_x_w_start(target_min, x)
    if n1 is None:
        return False, None, None
    n1 = ceil(n1) + 1
    n2 = solve_x_w_start(target_max, x)
    if n2 is None:
        return True, n1, None
    else:
        n2 = floor(n2) + 1

    solvable = n1 <= n2

    return solvable, n1, n2

if __name__ == '__main__':
    # part 1
    best = 0
    for i in range(250):
        y, solvable, _, _ = calc_max_height(i, input[1][0], input[1][1])
        if solvable:
            best = y

    print('result=', best)

    # part 2
    solvable_y = {}
    for i in range(-154, 250):
        y, solvable, n1, n2 = calc_max_height(i, input[1][0], input[1][1])
        if solvable:
            solvable_y[i] = n1, n2


    solvable_x = {}
    for i in range(1, input[0][1] + 1):
        solvable, n1, n2 = calc_x_solvable(i, input[0][0], input[0][1])
        if solvable:
            solvable_x[i] = n1, n2

    ivs = set()
    for x, (x_s, x_e) in solvable_x.items():
        for y, (y_s, y_e) in solvable_y.items():
            match = False

            for c in range(y_s, y_e + 1):
                if x_s <= c and (x_e is None or c <= x_e):
                    match = True
                    break

            if match:
                ivs.add((x, y))

    print('result=', len(ivs))
