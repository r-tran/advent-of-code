def calc_program(intcode, noun, verb):
	intcode = list(intcode)
	intcode[1], intcode[2] = noun, verb 
	supported_opcodes = set([1, 2, 99])

	i = 0
	while i < len(intcode) - 3:
		opcode = intcode[i]
		if opcode in supported_opcodes:
			a, b, = intcode[intcode[i + 1]], intcode[intcode[i + 2]]
			if opcode == 1:
				intcode[intcode[i + 3]] = a + b
			elif opcode == 2:
				intcode[intcode[i + 3]] = a * b
			else:
				break
		i += 4
	return intcode[0]
 
# part 1
intcode = [int(o) for o in open('input.txt', 'r').readline().split(',')]
print(calc_program(intcode, 12, 2))

# part 2
noun = verb = None
for i in range(100):
	for j in range(100):
		res = calc_program(intcode, i, j)
		if res == 19690720:
			print(100 * i + j)
