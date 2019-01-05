import sys

text = open(sys.argv[1]).readlines()
coordinates = [(int(line.split()[0].replace(',','')), int(line.split()[1])) for line in text]

def part2():
	m, n = float('-inf'), float('-inf')
	for a, b in coordinates:
		n, m = max(n, a), max(m, b)
	m, n = m + 1, n + 1
	regions = []

	grid = [[-1 for _ in range(n)] for _ in range(m)]
	for x in range(n):
		for y in range(m):
			curr = (x, y)
			if curr not in coordinates:
				distances = []
				shortest_distance = float('inf')
				for i in range(len(coordinates)):
					dist = manhattan_distance(curr, coordinates[i])
					distances.append(dist)
					if dist < shortest_distance:
						shortest_distance = dist
						closest_coordinate = i
				if distances.count(shortest_distance) == 1:
					grid[y][x] = closest_coordinate
				if sum(distances) < 10000:
					regions.append((y,x))
	
	coordinates_in_range = get_coordinates_in_range(coordinates)
	return len(regions) + len(coordinates_in_range)

def get_coordinates_in_range(coordinates):
	distances = []
	for i in range(len(coordinates)):
		distance = 0
		for x in coordinates:
			distance += manhattan_distance(coordinates[i], x)
		if distance < 10000:
			distances.append(i)
	return distances

def part1():
	m, n = float('-inf'), float('-inf')
	for a, b in coordinates:
		n, m = max(n, a), max(m, b)
	m, n = m + 1, n + 1

	grid = [[-1 for _ in range(n)] for _ in range(m)]
	for x in range(n):
		for y in range(m):
			curr = (x, y)
			if curr not in coordinates:
				distances = []
				shortest_distance = float('inf')
				for i in range(len(coordinates)):
					dist = manhattan_distance(curr, coordinates[i])
					distances.append(dist)
					if dist < shortest_distance:
						shortest_distance = dist
						closest_coordinate = i
				if distances.count(shortest_distance) == 1:
					grid[y][x] = closest_coordinate
	
	explore = list(range(len(coordinates)))
	invalid = landlocked(grid)
	for i in invalid:
		explore.remove(i)

	for i in range(len(coordinates)):
		x, y = coordinates[i]
		grid[y][x] = i

	areas = [flood_fill(el, grid) for el in explore]
	return max(areas)

def manhattan_distance(c1, c2):
	return abs(c1[0] - c2[0]) + abs(c1[1] - c2[1])

def landlocked(grid):
	locked = set()
	for y in range(len(grid)):
		locked.add(grid[y][0])
		locked.add(grid[y][len(grid[0]) - 1])

	for x in range(len(grid[0])):
		locked.add(grid[0][x])
		locked.add(grid[len(grid) - 1][x])
	locked.remove(-1)
	return locked

def flood_fill(el, grid):
	max_area = 0
	visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
	directions = [[-1, 0], [1,0],[0,-1],[0,1]]
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			if grid[i][j] == el and not visited[i][j]: 
				visited[i][j] = True
				area = 0
				stack = [(i,j)]
				while len(stack) > 0:
					curr_i, curr_j = stack.pop()
					area += 1
					for x, y in directions:
						next_i, next_j = x + curr_i, y + curr_j
						if 0 <= next_i < len(grid) and 0 <= next_j < len(grid[0]) and not visited[next_i][next_j] and grid[next_i][next_j] == el:
							stack.append((next_i, next_j))	
							visited[next_i][next_j] = True
				max_area = max(max_area, area)
	return max_area
					
print(part2())
