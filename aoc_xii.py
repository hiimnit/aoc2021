from typing import DefaultDict


input = [
    'zs-WO',
    'zs-QJ',
    'WO-zt',
    'zs-DP',
    'WO-end',
    'gv-zt',
    'iu-SK',
    'HW-zs',
    'iu-WO',
    'gv-WO',
    'gv-start',
    'gv-DP',
    'start-WO',
    'HW-zt',
    'iu-HW',
    'gv-HW',
    'zs-SK',
    'HW-end',
    'zs-end',
    'DP-by',
    'DP-iu',
    'zt-start',
]

START = 'start'
END   = 'end'

map = DefaultDict(list)

for line in input:
    a, b = line.split('-')
    map[a].append(b)
    map[b].append(a)

for k, v in map.items():
    print(k + ':\t', v)

def is_small(node: str) -> bool:
    return node == node.lower()

def step(map: map[str, list[str]], node: str, visited: list[str]):
    if node == END:
        return 1

    if is_small(node):
        visited.append(node)

    result = 0
    for n in map[node]:
        if n not in visited:
            result += step(map, n, list(visited))

    return result



def step2(map: map[str, list[str]], node: str, can_revisit: bool, visited: list[str]):
    if node == END:
        return [node]

    updated_visited = list(visited)
    if is_small(node):
        updated_visited.append(node)

    results = []
    for n in map[node]:
        if n not in visited:
            if can_revisit and is_small(node) and node != START:
                paths = step2(map, n, False, list(visited))
                if paths:
                    for path in paths:
                        results.append(f'{node}-{path}')
            paths = step2(map, n, can_revisit, list(updated_visited))
            if paths:
                for path in paths:
                    results.append(f'{node}-{path}')

    return list(set(results))


if __name__ == '__main__':
    # part 1
    result = step(map, START, [])
    print('result=', result)

    # part 2
    result = step2(map, START, True, [])
    print('result=', len(result))
