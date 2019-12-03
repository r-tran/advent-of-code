def dist(p, q):
	return abs(p[0] - q[0]) + abs(p[1] - q[1])

def get_path(wire):
	i = j = 0
	step = 1
	path = {}
	for visit in wire:
		dir, position = visit[0], int(visit[1:])
		if dir == 'U':
			for _ in range(position):
				i -= 1
				path[(i, j)] = step
				step += 1
		elif dir == 'D':
			for _ in range(position):
				i += 1
				path[(i, j)] = step
				step += 1
		elif dir == 'L':
			for _ in range(position):
				j -= 1
				path[(i, j)] = step
				step += 1
		elif dir == 'R':
			for _ in range(position):
				j += 1
				path[(i, j)] = step
				step += 1
	return path

def calculate_min_steps(intersections, steps_a, steps_b):
	min_steps = float('inf')
	for point in intersections:
		if point not in steps_a or point not in steps_b:
			raise Exception('Not an shared path intersection.')
		min_steps = min(min_steps, steps_a[point] + steps_b[point])
	return min_steps

wire1 = "R8,U5,L5,D3".split(',')
wire2 = "U7,R6,D4,L4".split(',')
path_wire1, path_wire2 = get_path(wire1), get_path(wire2)
intersections  = list(set(path_wire1.keys()) & set(path_wire2.keys()))
print(min([dist((0, 0), i) for i in intersections]))
print(calculate_min_steps(intersections, path_wire1, path_wire2))

wire1 = "R75,D30,R83,U83,L12,D49,R71,U7,L72".split(',')
wire2 = "U62,R66,U55,R34,D71,R55,D58,R83".split(',')
path_wire1, path_wire2 = get_path(wire1), get_path(wire2)
intersections  = list(set(path_wire1.keys()) & set(path_wire2.keys()))
print(min([dist((0, 0), i) for i in intersections]))
print(calculate_min_steps(intersections, path_wire1, path_wire2))


wire1 = "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51".split(',')
wire2 = "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7".split(',')
path_wire1, path_wire2 = get_path(wire1), get_path(wire2)
intersections  = list(set(path_wire1.keys()) & set(path_wire2.keys()))
print(min([dist((0, 0), i) for i in intersections]))
print(calculate_min_steps(intersections, path_wire1, path_wire2))

data = open('input.txt', 'r').readlines()
wire1, wire2 = data[0].strip().split(','), data[1].strip().split(',')
path_wire1, path_wire2 = get_path(wire1), get_path(wire2)
intersections  = list(set(path_wire1.keys()) & set(path_wire2.keys()))
print(min([dist((0, 0), i) for i in intersections]))
print(calculate_min_steps(intersections, path_wire1, path_wire2))
