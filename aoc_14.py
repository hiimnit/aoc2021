from typing import DefaultDict
from math import exp, floor

input = 'BNSOSBBKPCSCPKPOPNNK'
input = [c for c in input]

rules = {
    'HH': 'N',
    'CO': 'F',
    'BC': 'O',
    'HN': 'V',
    'SV': 'S',
    'FS': 'F',
    'CV': 'F',
    'KN': 'F',
    'OP': 'H',
    'VN': 'P',
    'PF': 'P',
    'HP': 'H',
    'FK': 'K',
    'BS': 'F',
    'FP': 'H',
    'FN': 'V',
    'VV': 'O',
    'PS': 'S',
    'SK': 'N',
    'FF': 'K',
    'PK': 'V',
    'OF': 'N',
    'VP': 'K',
    'KB': 'H',
    'OV': 'B',
    'CH': 'F',
    'SF': 'F',
    'NH': 'O',
    'NC': 'N',
    'SP': 'N',
    'NN': 'F',
    'OK': 'S',
    'BB': 'S',
    'NK': 'S',
    'FH': 'P',
    'FC': 'S',
    'OB': 'P',
    'VS': 'P',
    'BF': 'S',
    'HC': 'V',
    'CK': 'O',
    'NP': 'K',
    'KV': 'S',
    'OS': 'V',
    'CF': 'V',
    'FB': 'C',
    'HO': 'S',
    'BV': 'V',
    'KS': 'C',
    'HB': 'S',
    'SO': 'N',
    'PH': 'C',
    'PN': 'F',
    'OC': 'F',
    'KO': 'F',
    'VF': 'V',
    'CS': 'O',
    'VK': 'O',
    'FV': 'N',
    'OO': 'K',
    'NS': 'S',
    'KK': 'C',
    'FO': 'S',
    'PV': 'S',
    'CN': 'O',
    'VC': 'P',
    'SS': 'C',
    'PO': 'P',
    'BN': 'N',
    'PB': 'N',
    'PC': 'H',
    'SH': 'K',
    'BH': 'F',
    'HK': 'O',
    'VB': 'P',
    'NV': 'O',
    'NB': 'C',
    'CP': 'H',
    'NO': 'K',
    'PP': 'N',
    'CC': 'S',
    'CB': 'K',
    'VH': 'H',
    'SC': 'C',
    'KC': 'N',
    'SB': 'B',
    'BP': 'P',
    'KP': 'K',
    'SN': 'H',
    'KF': 'K',
    'KH': 'B',
    'HV': 'V',
    'HS': 'K',
    'NF': 'B',
    'ON': 'H',
    'BO': 'P',
    'VO': 'K',
    'OH': 'C',
    'HF': 'O',
    'BK': 'H',
}

mem = {k: [k[0] + v + k[1],] for k, v in rules.items()}

# TODO navrat k puvodnimu planu
# k0: ['xxx', 'xxxxx', 'xxxxxxxxxxx', ...]
# k1: ['xxx', 'xxxxx', 'xxxxxxxxxxx', ...]
# k2: ['xxx', 'xxxxx', 'xxxxxxxxxxx', ...]
# ...

def expand(polymer: list[str], depth: int) -> list[str]:
    depth -= 1
    result = polymer[0]
    for l, r in zip(polymer, polymer[1:]):
        new_polymer = ''
        if len(mem[l + r]) > depth:
            new_polymer = mem[l + r][depth]
        else:
            new_polymer = expand(l + r, depth)
            new_polymer = expand(new_polymer, 1)
            mem[l + r].append(new_polymer)
        result += new_polymer[1:]
        
    return result


if __name__ == '__main__':
    # part 1
    polymer = list(input)
    for _ in range(10):
        new_polymer = []
        for l, r in zip(polymer, polymer[1:]):
            new_polymer.append(l)
            new_polymer.append(rules[l + r])
        new_polymer.append(polymer[-1])
        polymer = new_polymer

    counter = DefaultDict(int)
    for c in polymer:
        counter[c] += 1

    print(counter.keys())
    result = max(counter.values()) - min(counter.values())
    print('result=', result)

    # part 2
    # "memoization"
    # kinda meh, memorize the first 20 levels for each combination
    # why 20? still pretty fast, ~ 1 second
    # expand input once
    # then directly count instead of expanding since we do not need the result
    for rule in rules.keys():
        print('preparing', rule)
        polymer = list(rule)
        expand(polymer, 20)

    polymer = list(input)
    polymer = expand(polymer, 20)
    print('expanded 20', len(polymer))

    keys = ['B', 'N', 'F', 'V', 'C', 'S', 'P', 'K', 'O', 'H']

    counter_mem = {}
    for k, v in mem.items():
        counter = [0] * 10
        for c in v[-1]:
            counter[keys.index(c)] += 1
        counter_mem[k] = counter

    print('prepared counter mem')

    counter = [0] * 10
    for l, r in zip(polymer, polymer[1:]):
        expanded_counted = counter_mem[l + r]
        for i, n in enumerate(expanded_counted):
            counter[i] += n

        counter[keys.index(r)] -= 1
    counter[keys.index(polymer[-1])] += 1

    result = max(counter) - min(counter)
    print('result=', result)

