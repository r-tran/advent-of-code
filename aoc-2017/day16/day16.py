from collections import deque

programs = deque(list('abcdefghijklmnop'))
moves = open('input/input.txt', 'r').readline().split(',')

def parse_move(move):
	a = []
	b = []
	i = 1 
	while move[i] != '/':
		a.append(move[i])
		i += 1
	i += 1 
	b.append(move[i:])
	return int(''.join(a)), int(''.join(b))

def dance(n):
	num = 0
	configs = []
	while True:
		for move in moves:
			if move[0] == 's':
				programs.rotate(int(move[1:]))
			elif move[0] == 'x':
				i, j = parse_move(move) 
				programs[i], programs[j] = programs[j], programs[i]	
			elif move[0] == 'p':
				i = programs.index(move[1])
				j = programs.index(move[3])
				programs[i], programs[j] = programs[j], programs[i]	
			else:
				print('not a valid move')
		
		config = ''.join(list(programs))
		if config not in configs:
			configs.append(config)
		else:
			print('num: {}'.format(num))
			print('Configs {}'.format(configs))
			return configs[(n -1) % len(configs)] 
		num += 1

print(dance(1000000000))
