instructions = ['S', 'U', 'L', 'D', 'R']
steps = {'S':1, 'U':-1, 'L':0, 'D':0,'R':0}
coordinates = {(0,0):1}

def update_cycle():
	for item in steps:
		if item != 'S':
			steps[item] += 2

def add_coordinate(x,y, value):
	coordinates[(x,y)] = value

def get_neighbor_values(x, y):
	combined = 0
	if (x - 1, y) in coordinates:
		combined += coordinates[(x - 1, y)]
	if (x + 1, y) in coordinates:
		combined += coordinates[(x + 1, y)]
	if (x, y - 1) in coordinates:
		combined += coordinates[(x, y - 1)]
	if (x, y + 1) in coordinates:
		combined += coordinates[(x, y + 1)]
	if (x - 1, y - 1) in coordinates:
		combined += coordinates[(x - 1, y - 1)]
	if (x - 1, y + 1) in coordinates:
		combined += coordinates[(x - 1, y + 1)]
	if (x + 1, y - 1) in coordinates:
		combined += coordinates[(x + 1, y - 1)]
	if (x + 1, y + 1) in coordinates:
		combined += coordinates[(x + 1, y + 1)]

	return combined

def spiral(n):
	x = 0
	y = 0
	i = 0
	start = 0

	while True:
		if start > n:
			break
		if instructions[i] == 'S':
			update_cycle()
			y += 1
			start = get_neighbor_values(x,y)
			add_coordinate(x,y,start)
		elif instructions[i] == 'U':
			for j in range(steps[instructions[i]]):
				if start <= n:
					x -= 1
					start = get_neighbor_values(x,y)
					add_coordinate(x,y,start)
		elif instructions[i] == 'L':
			for j in range(steps[instructions[i]]):
				if start <= n:	
					y -= 1
					start = get_neighbor_values(x,y)
					add_coordinate(x,y,start)
		elif instructions[i] == 'D':
			for j in range(steps[instructions[i]]):
				if start <= n:			
					x += 1
					start = get_neighbor_values(x,y)
					add_coordinate(x,y,start)
		elif instructions[i] == 'R':
			for j in range(steps[instructions[i]]):
				if start <= n:
					y += 1
					start = get_neighbor_values(x,y)
					add_coordinate(x,y,start)
	 	
		i = (i + 1) % len(instructions)

	print('Max value: {}'.format(start))
	#print(coordinates)
	return (x, y)

spiral(277678)