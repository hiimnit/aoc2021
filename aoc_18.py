from math import floor, ceil

input = [
    [[[3,9],[7,2]],[[8,4],[[5,6],0]]],
    [[[1,[4,9]],[[1,8],[1,5]]],[[[2,6],[6,7]],[[4,6],[9,0]]]],
    [[[[9,2],1],[[0,7],[9,6]]],[[5,9],[7,[6,9]]]],
    [8,9],
    [[4,[6,1]],[2,[[6,7],2]]],
    [[6,[[4,1],5]],[4,9]],
    [[[0,6],[8,[8,5]]],[6,9]],
    [[0,[1,0]],[[8,[7,4]],[[1,1],[5,0]]]],
    [[[1,[0,1]],6],[1,9]],
    [[2,[[9,0],[6,1]]],[[8,4],[5,7]]],
    [[[[5,3],[0,9]],[1,[0,7]]],[[9,0],[2,[2,0]]]],
    [[2,[2,[6,8]]],[[9,[5,4]],[4,[3,4]]]],
    [[[[4,0],[7,0]],[[4,8],[5,8]]],[[[7,2],[2,2]],[[3,3],3]]],
    [[5,0],5],
    [[8,[[5,0],2]],[6,[5,1]]],
    [[[9,[8,8]],[8,7]],[[[4,2],4],[[5,1],[4,8]]]],
    [[[[1,1],3],5],9],
    [[[[1,7],[6,5]],5],[[0,6],0]],
    [[9,6],2],
    [[[2,[0,8]],[8,[2,1]]],5],
    [[[9,[3,7]],3],[0,[5,9]]],
    [[[2,[1,7]],6],[[7,[8,2]],[[8,2],8]]],
    [[[[1,2],1],5],2],
    [4,[8,[3,9]]],
    [[[[8,9],[6,0]],[[1,6],7]],8],
    [[2,[8,1]],3],
    [[2,2],[[8,[0,2]],[[5,0],5]]],
    [9,[2,[[6,1],[8,9]]]],
    [[4,[[6,6],4]],[[[9,3],[3,1]],5]],
    [[[7,8],1],0],
    [[[8,8],[[1,0],7]],[4,6]],
    [9,8],
    [[[[4,2],9],[[9,9],7]],[7,[9,[5,8]]]],
    [[4,[4,[3,3]]],8],
    [0,2],
    [[4,[5,5]],[9,[[6,9],4]]],
    [[[7,3],[[1,2],6]],[[[2,4],[6,7]],[[5,0],9]]],
    [[[[2,0],5],[4,5]],[[[6,5],[6,0]],[1,[3,4]]]],
    [[3,[6,8]],[[[3,0],0],[[2,8],7]]],
    [[[4,[6,2]],[9,[4,1]]],[8,[3,4]]],
    [[[6,[6,8]],[7,[2,0]]],[4,[[8,7],[1,6]]]],
    [2,[0,[4,0]]],
    [[[[0,5],1],8],[[9,[0,3]],3]],
    [[[3,[5,2]],[3,[3,2]]],[[[7,3],1],7]],
    [1,[[[1,8],[1,7]],0]],
    [[8,6],[[0,4],4]],
    [[[8,2],[4,6]],3],
    [5,[[[7,5],[4,5]],[0,2]]],
    [[3,[3,6]],6],
    [[[[6,8],[5,7]],[[7,3],5]],[[8,[4,8]],8]],
    [[[[5,8],[3,1]],[[3,7],[7,0]]],[[9,7],0]],
    [[2,[[5,3],8]],0],
    [0,[2,8]],
    [[8,9],[[[2,2],[4,7]],[[4,0],1]]],
    [[[[3,0],8],[[7,3],[6,1]]],[[3,8],[4,2]]],
    [[[[6,7],[4,3]],[[3,9],5]],8],
    [[[7,7],[[3,4],7]],[[[0,4],1],9]],
    [[[7,5],5],[[2,[9,9]],[0,[3,5]]]],
    [[[[3,3],[6,1]],[5,8]],[[4,7],[8,1]]],
    [[[0,[7,3]],[6,[7,2]]],[[0,8],7]],
    [[[2,7],[9,7]],[8,[3,8]]],
    [[[0,2],6],[[9,[6,5]],[[3,9],1]]],
    [[7,[[3,4],[2,8]]],[[[4,1],4],7]],
    [[3,[[3,4],6]],[[3,9],[[4,5],[3,0]]]],
    [[[5,[5,1]],[2,4]],[1,[[1,6],6]]],
    [[[5,6],[[1,3],[5,0]]],[[[4,1],8],[5,5]]],
    [[[[2,0],7],[[8,9],1]],[[[4,0],[1,6]],1]],
    [[[2,0],[[4,2],[9,9]]],[4,9]],
    [[[[1,9],6],2],[[5,4],[2,4]]],
    [[[[4,1],[4,5]],[[2,3],2]],[3,[[8,8],1]]],
    [[[[8,1],0],[2,2]],[[2,[7,1]],1]],
    [[[7,4],[[1,3],5]],[[6,8],[[0,0],2]]],
    [[[1,2],8],[[[1,7],[4,0]],[[8,2],8]]],
    [[[0,8],[3,6]],[[[5,3],7],[9,7]]],
    [[4,6],[[[7,9],[7,5]],[[4,6],[8,4]]]],
    [[[[7,3],0],[[6,2],[7,2]]],[9,[[8,0],3]]],
    [[[3,0],1],[[2,3],1]],
    [[[5,[8,6]],[[1,2],2]],[[[1,4],6],[5,[7,1]]]],
    [[[[1,5],8],[0,0]],4],
    [[[7,[6,8]],3],[[5,1],[[2,8],[4,6]]]],
    [3,[[[5,8],[4,5]],[[7,7],8]]],
    [[6,[7,[8,2]]],[[9,0],0]],
    [[[8,[7,6]],1],[[2,4],6]],
    [[[[0,4],2],[0,7]],[6,6]],
    [1,[[1,9],[9,3]]],
    [[[[5,2],[5,3]],[[9,0],4]],2],
    [[[[5,5],3],[7,[1,2]]],[6,[7,2]]],
    [[[[2,1],3],8],[[2,[8,2]],[7,4]]],
    [[8,[9,[1,8]]],[[[4,4],[0,6]],[6,3]]],
    [[[1,6],[1,[2,5]]],0],
    [[[[0,1],[7,2]],[[7,2],3]],[2,[[7,8],[0,7]]]],
    [[[[1,8],8],[[5,7],[3,4]]],[[[2,5],[7,4]],[[8,4],9]]],
    [[[2,2],[5,[1,0]]],[[[6,6],[3,0]],[[8,5],5]]],
    [[[[8,2],[4,8]],[9,4]],[[8,[7,9]],0]],
    [[3,[5,[2,4]]],[[[8,1],0],[[0,4],[4,5]]]],
    [[5,[9,[3,8]]],[4,[1,[5,2]]]],
    [[[3,[0,6]],[7,[8,7]]],[[6,8],[[8,7],0]]],
    [[[[0,2],5],[4,6]],3],
    [[6,7],[[1,[4,6]],9]],
    [7,[3,[[8,8],5]]],
]

class Type:
    LEFT = 0
    RIGHT = 1

class SnailfishNumber:
    def __init__(self, left: 'SnailfishNumber' or int, right: 'SnailfishNumber' or int,
                 parent: 'SnailfishNumber' or None) -> None:
        self.left: SnailfishNumber or int = left
        self.right: SnailfishNumber or int = right
        self.parent: SnailfishNumber or None = parent

    def __repr__(self) -> str:
        # return f'<SnailfishNumber left={self.left} right={self.right}>'
        return f'[{self.left}, {self.right}]'

    def __add__(self, other: 'SnailfishNumber') -> 'SnailfishNumber':
        sn = SnailfishNumber(self, other, None)
        self.parent = sn
        other.parent = sn

        while True:
            exploded = sn.explode()
            if exploded:
                continue
        
            split = sn.split()
            if split:
                continue
        
            break

        return sn

    def find_left_neighbor(self) -> 'SnailfishNumber' or None:
        last = self
        curr = last.parent
        
        while curr is not None and curr.left == last:
            last, curr = curr, curr.parent

        if curr is None:
            return None, None

        if isinstance(curr.left, int):
            return curr, Type.LEFT

        last, curr = curr, curr.left

        while isinstance(curr.right, SnailfishNumber):
            curr = curr.right

        return curr, Type.RIGHT

    def find_right_neighbor(self) -> 'SnailfishNumber' or None:
        last = self
        curr = last.parent
        
        while curr is not None and curr.right == last:
            last, curr = curr, curr.parent

        if curr is None:
            return None, None

        if isinstance(curr.right, int):
            return curr, Type.RIGHT

        last, curr = curr, curr.right

        while isinstance(curr.left, SnailfishNumber):
            curr = curr.left

        return curr, Type.LEFT

    def explode(self, depth: int = 0) -> bool:
        if depth == 4: # TODO and self.left and self.right are ints!
            if not isinstance(self.left, int) or not isinstance(self.right, int):
                raise NotImplementedError()

            sn, type = self.find_left_neighbor()
            if sn:
                if type == Type.LEFT:
                    sn.left += self.left
                else:
                    sn.right += self.left

            sn, type = self.find_right_neighbor()
            if sn:
                if type == Type.LEFT:
                    sn.left += self.right
                else:
                    sn.right += self.right

            if self == self.parent.left:
                self.parent.left = 0
            else:
                self.parent.right = 0

            return True

        if isinstance(self.left, SnailfishNumber):
            exploded = self.left.explode(depth + 1)
            if exploded:
                return True

        if isinstance(self.right, SnailfishNumber):
            exploded = self.right.explode(depth + 1)
            if exploded:
                return True

        return False

    def split(self) -> bool:
        if isinstance(self.left, int) and self.left > 9:
            self.left = SnailfishNumber(floor(self.left / 2), ceil(self.left / 2), self)
            return True
        
        if isinstance(self.left, SnailfishNumber):
            split = self.left.split()
            if split:
                return True

        if isinstance(self.right, int) and self.right > 9:
            self.right = SnailfishNumber(floor(self.right / 2), ceil(self.right / 2), self)
            return True
        
        if isinstance(self.right, SnailfishNumber):
            split = self.right.split()
            if split:
                return True

        return False

    def get_magnitude(self) -> int:
        left = 3 * (self.left if isinstance(self.left, int) else self.left.get_magnitude())
        right = 2 * (self.right if isinstance(self.right, int) else self.right.get_magnitude())
        return left + right

    @staticmethod
    def parse(input: any, parent: 'SnailfishNumber' or None = None) -> 'SnailfishNumber' or int:
        if isinstance(input, int):
            return input
        if isinstance(input, list):
            sn = SnailfishNumber(None, None, parent)
            sn.left = SnailfishNumber.parse(input[0], sn)
            sn.right = SnailfishNumber.parse(input[1], sn)
            return sn
        
        raise NotImplementedError()

if __name__ == '__main__':
    # part 1
    sn = SnailfishNumber.parse(input[0])
    for i in input[1:]:
        sn += SnailfishNumber.parse(i)
        # print(sn)

    print('result=', sn.get_magnitude())

    # part 2
    best = None
    for i, sn in enumerate(input):
        for j, other in enumerate(input):
            sum = SnailfishNumber.parse(sn) + SnailfishNumber.parse(other)
            magnitude = sum.get_magnitude()
            if not best or magnitude > best:
                best = magnitude

    print('result=', best)

