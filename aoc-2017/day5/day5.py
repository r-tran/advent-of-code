instructions = [int(i) for i  in open('input/input.txt', 'r').readlines()]

def count_num_steps(instructions):
	i = 0
	n_steps = 0
	while i < len(instructions):
		last_index = i
		i = i + instructions[i]
		if instructions[last_index] >= 3:
			instructions[last_index] -= 1
		else:
			instructions[last_index] += 1
		n_steps += 1
	return n_steps

ins = [0, 3, 0, 1, -3]
print(count_num_steps(instructions))
