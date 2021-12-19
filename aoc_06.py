input = [2,5,3,4,4,5,3,2,3,3,2,2,4,2,5,4,1,1,4,4,5,1,2,1,5,2,1,5,1,1,1,2,4,3,3,1,4,2,3,4,5,1,2,5,1,2,2,5,2,4,4,1,4,5,4,2,1,5,5,3,2,1,3,2,1,4,2,5,5,5,2,3,3,5,1,1,5,3,4,2,1,4,4,5,4,5,3,1,4,5,1,5,3,5,4,4,4,1,4,2,2,2,5,4,3,1,4,4,3,4,2,1,1,5,3,3,2,5,3,1,2,2,4,1,4,1,5,1,1,2,5,2,2,5,2,4,4,3,4,1,3,3,5,4,5,4,5,5,5,5,5,4,4,5,3,4,3,3,1,1,5,2,4,5,5,1,5,2,4,5,4,2,4,4,4,2,2,2,2,2,3,5,3,1,1,2,1,1,5,1,4,3,4,2,5,3,4,4,3,5,5,5,4,1,3,4,4,2,2,1,4,1,2,1,2,1,5,5,3,4,1,3,2,1,4,5,1,5,5,1,2,3,4,2,1,4,1,4,2,3,3,2,4,1,4,1,4,4,1,5,3,1,5,2,1,1,2,3,3,2,4,1,2,1,5,1,1,2,1,2,1,2,4,5,3,5,5,1,3,4,1,1,3,3,2,2,4,3,1,1,2,4,1,1,1,5,4,2,4,3]

def p1_progress_day(fishes: list[int]):
    spawn = 0
    for i, fish in enumerate(fishes):
        if fish == 0:
            fishes[i] = 7
            spawn += 1
        fishes[i] -= 1
    
    fishes += [8] * spawn

def p2_progress_day(fishes: list[int]):
    spawn = fishes[0]

    for i in range(1, 7):
        fishes[i-1] = fishes[i]
    fishes[6] = spawn + fishes[7]
    fishes[7] = fishes[8]
    fishes[8] = spawn

if __name__ == '__main__':
    # part 1
    fishes = list(input)
    for i in range(80):
        p1_progress_day(fishes)
    
    print('result=', len(fishes))
    
    # part 2
    fishes = [0] * 9 
    
    for fish in input:
        fishes[fish] += 1

    for i in range(256):
        p2_progress_day(fishes)
    
    print('result=', sum(fishes))
