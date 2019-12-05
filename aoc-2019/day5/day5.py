program = list(map(int, open('input.txt', 'r').readline().strip().split(',')))
ptr = 0 
input_code = 5
output_codes = []

def helper(program, ptr, param_modes):
	a_mode = param_modes.pop() if len(param_modes) > 0 else 0
	b_mode = param_modes.pop() if len(param_modes) > 0 else 0

	a = program[ptr + 1] if a_mode == 1 else program[program[ptr + 1]]
	b = program[ptr + 2] if b_mode == 1 else program[program[ptr + 2]]
	c = program[ptr + 3] if ptr + 3 < len(program) else None

	return (a, b, c)

while program[ptr] != 99:
	instruction = str(program[ptr])
	n = len(instruction)
	opcode, param_modes = int(instruction[n -2:n]), list(map(int, instruction[:-2]))
	
	if opcode == 1:
		a, b, c = helper(program, ptr, param_modes)
		program[c] = a + b
	elif opcode == 2:
		a, b, c = helper(program, ptr, param_modes)
		program[c] = a * b
	elif opcode == 3:
		program[program[ptr + 1]] = input_code
	elif opcode == 4:
		output_codes.append(program[program[ptr + 1]])
	elif opcode == 5:
		a, b, _ = helper(program, ptr, param_modes)
		if a != 0:
			ptr = b
			continue
	elif opcode == 6:
		a, b, _ = helper(program, ptr, param_modes)
		if a == 0:
			ptr = b
			continue
	elif opcode == 7:
		a, b, c = helper(program, ptr, param_modes)
		program[c] = 1 if a < b else 0
	elif opcode == 8:
		a, b, c = helper(program, ptr, param_modes)
		program[c] = 1 if a == b else 0
	else:
		raise Exception('Unknown opcode: {}'.format(opcode))
	
	step = 2 if opcode == 3 or opcode == 4 else 4
	ptr += step
	print(ptr)

print(output_codes)
