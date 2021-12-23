from math import sqrt, floor, ceil

input = 'target area: x=111..161, y=-154..-101'
input = [(111, 161), (-101, -154)]

# sum = (n + 1) * n / 2
# 2 * sum = n**2 + n
# 0 = n**2 + n - 2 * sum

# D = b**2 - 4 * a * c
# D = 1 + 8 * sum

# n1 = (-1 - sqrt(D)) / 2
# n2 = (-1 + sqrt(D)) / 2

def solve(s: int):
    return (-1 + sqrt(1 + 8 * s)) * .5

def linear_sum(n: int) -> int:
    return (n + 1) * n / 2

def calc_max_height(y: int, target_min: int, target_max: int):
    if y < 0:
        raise NotImplementedError()
    
    max_y = linear_sum(y)

    n1 = solve(max_y - target_min)
    n2 = solve(max_y - target_max)

    # TODO what if n1 or n2 already are whole numbers?
    solvable = ceil(n2) - floor(n1) > 1 or floor(n1) == n1 or floor(n2) == n2

    return max_y, solvable

if __name__ == '__main__':
    # part 1
    best = 0
    for i in range(1000):
        y, solvable = calc_max_height(i, input[1][0], input[1][1])
        print('y', y, 'solvable', solvable)
        if solvable:
            best = y

    print('result=', best)

    # part 2
    ivs = set()

    print(solve(101))
    print(linear_sum(floor(solve(101))))
    print(linear_sum(ceil(solve(101))))

    print(solve(154))
    print(linear_sum(floor(solve(154))))
    print(linear_sum(ceil(solve(154))))

    print(solve(111))
    print(linear_sum(floor(solve(111))))
    print(solve(161))
    print(linear_sum(floor(solve(161))))
    # TODO
    # 0. combine part 1 y with all possible xs
    # 1. add direct jumps
    # > thats max X
    # 2. find min X
    # > test everything in between?
    

    print('result=', len(ivs))
    pass

# solving x
# 1. 

# S..............................................................
# ...............................................................
# ...............................................................
# ...............................................................
# .................#.............................................
# ....................TTTTTTTTTTT................................
# ....................TTTTTTTTTTT................................
# ....................TTTTTTTTTTT................................
# ....................TTTTTTTTTTT................................
# ....................TTTTTTTTTTT..#.............................
# ....................TTTTTTTTTTT................................
# ...............................................................
# ...............................................................
# ...............................................................
# ...............................................................
# ................................................#..............
# ...............................................................
# ...............................................................
# ...............................................................
# ...............................................................
# ...............................................................
# ...............................................................
# ..............................................................#