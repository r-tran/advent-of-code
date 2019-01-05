def execute_instructions(instruction):
	global max_value
	operation = 'inc' if 'inc' in instruction else 'dec'
	register_name = instruction.split()[0]
	value = int(instruction.split()[-1])
	if operation == 'inc':
		registers[register_name] += value
	else:
		registers[register_name] -= value
	if registers[register_name] > max_value:
		max_value = registers[register_name]

lines = open('input/input.txt', 'r').readlines()
registers = {}
instructions = [line.strip('\n').split("if ")[0] for line in lines]
conditions = [line.strip('\n').split("if ")[1] for line in lines]
max_value = 0

for line in lines:
	registers[line.split()[0]] = 0

for i in range(len(conditions)):
	lhs_operand = conditions[i].split()[0]
	rhs_operand = int(conditions[i].split()[-1])

	if " < " in conditions[i]:
		if registers[lhs_operand] < rhs_operand:
			execute_instructions(instructions[i])
	elif " <= " in conditions[i]:
		if registers[lhs_operand] <= rhs_operand:
			execute_instructions(instructions[i])		
	elif " > " in conditions[i]:
		if registers[lhs_operand] > rhs_operand:
			execute_instructions(instructions[i])
	elif " >= " in conditions[i]:
		if registers[lhs_operand] >= rhs_operand:
			execute_instructions(instructions[i])
	elif " != " in conditions[i]:
		if registers[lhs_operand] != rhs_operand:
			execute_instructions(instructions[i])
	elif " == " in conditions[i]:
		if registers[lhs_operand] == rhs_operand:
			execute_instructions(instructions[i])
	else:
		print('operator not found')

print(max(registers, key=registers.get))
print(max(registers.values()))
print('Highest value: {}'.format(max_value))