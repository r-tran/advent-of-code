import sys 
from collections import defaultdict

lines = open(sys.argv[1]).readlines()

# Operations
def addr(reg, a, b, c):
    reg[c] = reg[a] + reg[b]
def addi(reg, a, b, c):
    reg[c] = reg[a] + b
def mulr(reg, a, b, c):
    reg[c] = reg[a] * reg[b]
def muli(reg, a, b, c):
    reg[c] = reg[a] * b
def banr(reg, a, b, c):
    reg[c] = reg[a] & reg[b]
def bani(reg, a, b, c):
    reg[c] = reg[a] & b
def borr(reg, a, b, c):
    reg[c] = reg[a] | reg[b]
def bori(reg, a, b, c):
    reg[c] = reg[a] | b
def setr(reg, a, b, c):
    reg[c] = reg[a]
def seti(reg, a, b, c):
    reg[c] = a
def gtir(reg, a, b, c):
    reg[c] = 1 if a > reg[b] else 0
def gtri(reg, a, b, c):
    reg[c] = 1 if reg[a] > b else 0
def gtrr(reg, a, b, c):
    reg[c] = 1 if reg[a] > reg[b] else 0
def eqir(reg, a, b, c):
    reg[c] = 1 if a == reg[b] else 0
def eqri(reg, a, b, c):
    reg[c] = 1 if reg[a] == b else 0
def eqrr(reg, a, b, c):
    reg[c] = 1 if reg[a] == reg[b] else 0

before_registers = []
after_registers = []
instructions = []
for i in range(len(lines)):
    if lines[i].startswith('Before: '):
        before_registers.append(list(map(int, lines[i].split(': ')[1][1:-2].split(','))))
        instructions.append(list(map(int, lines[i+1].split())))
        after_registers.append(list(map(int, lines[i+2].split(':  ')[1][1:-2].split(','))))


instruction_text= ['addr','addi','mulr','muli','banr','bani','borr','bori','setr','seti','gtir','gtrr','eqir','eqri','eqrr']
opcodes = { i : set(instruction_text) for i in range(16) }

def execute(opcode, a, b, c, register_state_before, register_state_after):
	n = len(before_registers)
	op = ''
	remove = []
	if opcode in opcodes:
		for opname in opcodes[opcode]:
			register_state = list(register_state_before)
			if opname == 'addr':
				addr(register_state, a, b, c)
				op = 'addr'
			elif opname == 'addi':
				addi(register_state, a, b, c)
				op = 'addi'
			elif opname == 'mulr':
				mulr(register_state, a, b, c)
				op = 'mulr'
			elif opname == 'muli':
				muli(register_state, a, b, c)
				op = 'muli'
			elif opname == 'banr':
				banr(register_state, a, b, c)
				op = 'banr'
			elif opname == 'bani':
				bani(register_state, a, b, c)
				op = 'bani'
			elif opname == 'borr':
				borr(register_state, a, b, c)
				op = 'borr'
			elif opname == 'bori':
				bori(register_state, a, b, c)
				op = 'bori'
			elif opname == 'setr':
				setr(register_state, a, b, c)
				op = 'setr'
			elif opname == 'seti':
				seti(register_state, a, b, c)
				op = 'seti'
			elif opname == 'gtir':
				gtir(register_state, a, b, c)
				op = 'gtir'
			elif opname == 'gtrr':
				gtrr(register_state, a, b, c)
				op = 'gtrr'
			elif opname == 'eqir':
				eqir(register_state, a, b, c)
				op = 'eqir'
			elif opname == 'eqri':
				eqri(register_state, a, b, c)
				op = 'eqri'
			elif opname == 'eqrr':
				eqrr(register_state, a, b, c)
				op = 'eqrr'
			else:
				raise Error('Wrong opname')

			if register_state != register_state_after:
				remove.append(op)
		for opname in remove:
			opcodes[opcode].remove(opname)

def part2():
	n = len(before_registers)
	for i in range(n):
		opcode = instructions[i][0]
		a, b, c = instructions[i][1], instructions[i][2], instructions[i][3]
		register_before, register_after = before_registers[i], after_registers[i]
		execute(opcode, a, b, c, register_before, register_after)
	
	update_opcodes()
	return opcodes
	
		

def update_opcodes():
	explore = [(opcode, list(opcodes[opcode])[0]) for opcode in opcodes if len(opcodes[opcode]) == 1]
	found_opcodes = set()
	while len(explore) > 0:
		curr_opcode, curr_opname = explore.pop()
		found_opcodes.add(curr_opcode)
		for opcode in opcodes:
			if opcode == curr_opcode:
				continue
			if curr_opname in opcodes[opcode]:
				opcodes[opcode].remove(curr_opname)
				if len(opcodes[opcode]) == 1 and opcode not in found_opcodes:
					explore.append((opcode, next(iter(opcodes[opcode]))))
        
print(part2())
