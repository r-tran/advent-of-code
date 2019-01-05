import itertools
import sys

lines = open(sys.argv[1]).readlines()
nums = map(int, lines)

def day1():
    freq = 0
    freq_saved = set([0])
    for num in itertools.cycle(nums): 
        freq += num
        if freq in freq_saved:
            return freq
        freq_saved.add(freq)

print(day1())
