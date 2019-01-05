def interpret_operand(op):
	if op in registers:
		return registers[op]
	else:
		return int(op)

instructions = [line.split()[0] for line in open('input/input.txt', 'r').readlines()]
targets = [line.split()[1] for line in open('input/input.txt', 'r').readlines()]
operands = []
for line in open('input/input.txt', 'r').readlines():
	if len(line.split()) == 3:
		operands.append(line.split()[2])
	else:
		operands.append(0)

registers = {}
for r in set(targets):
	registers[r] = 0

freq = 0
n = len(instructions)
i = 0
while i < n:
	instr = instructions[i] 
	reg = targets[i]
	val = interpret_operand(operands[i])
	#print('{} {} {}'.format(instr, reg, val))
	#print('reg[{}]:{}'.format(reg, registers[reg]))

	if instr == 'set':
		registers[reg] = val
	elif instr == 'add':
		registers[reg] += val
	elif instr == 'mul':
		registers[reg] *= val
	elif instr == 'snd':
		freq = registers[reg]
		#print('Freq: %s' % freq)
	elif instr == 'mod':
		registers[reg] = registers[reg] % val
	elif instr == 'rcv':
		if registers[reg] != 0:
			print(freq)
			break
	elif instr == 'jgz':
		if registers[reg] > 0:
			i += val
			continue
	else:
		print('Instruction not recognized')

	i += 1
	#print(registers)
