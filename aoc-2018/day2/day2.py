import sys
from collections import Counter
lines = open(sys.argv[1]).readlines()

def part1():
    count_two, count_three = 0, 0
    counters = [Counter(line) for line in lines]
    for counter in counters:
        has_count_two, has_count_three = False, False
        for letter in counter:
            if counter[letter] == 2 and not has_count_two:
                count_two += 1
                has_count_two = True
            if counter[letter] == 3 and not has_count_three:
                count_three += 1
                has_count_three = True
    
    return count_two * count_three

def part2():
    for i in range(len(lines)):
        for j in range(i, len(lines)):
            if i != j:
                differ_by_one, chars = diff(lines[i], lines[j])
                if differ_by_one: 
                    print('found')
                    return chars


def diff(s, t):
    already_has_one_mismatch = False
    mismatch_index = -1
    mismatch_string = None
    
    for i in range(len(s)):
        if s[i] != t[i]:
            if (already_has_one_mismatch):
                return (False, None)

            already_has_one_mismatch = True
            mismatch_index = i
            mismatch_string = s

    print('mismatch is {}'.format(mismatch_string))
    print('mismatch at {}'.format(mismatch_index))

    return  (True, s[:mismatch_index] + s[mismatch_index+1:])

print(part2())
