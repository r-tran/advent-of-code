import sys
from collections import deque

lines = open(sys.argv[1]).readlines()
initial_state = deque(list(lines[0].split()[2]))
rules = {line.split()[0] : line.split()[2] for line in lines[2:]}

def part1(n_generations, plants, ruleset):
    offset = 0
    for _ in range(n_generations):
        state_transitions = {}
        offset += 2
        plants.appendleft('.')
        plants.appendleft('.')
        plants.append('.')
        plants.append('.')
        for i in range(2, len(plants) - 2):
            state_changes, res = interpret_state(ruleset, plants, i)
            if state_changes:
                state_transitions[i] = res
            else:
                print('state change not found')
                state_transitions[i] = '.'
        for i in state_transitions:
            plants[i] = state_transitions[i]
    
    total = 0 
    for i in range(len(plants)):
        if plants[i] == '#':
            total += (i - offset)
    return total

def interpret_state(ruleset, state, i):
    for rule in ruleset:
        rule_i = 0
        for j in range(i - 2, i + 3):
            if state[j] != rule[rule_i]: 
                break
            rule_i += 1
        if rule_i == 5:
            #print('Match at i: {} with rule: {}'.format(i - 2, rule))
            return (True, ruleset[rule])
    return (False, None)

print(part1(20, initial_state, rules))
