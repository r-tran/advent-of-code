def calculate_power_level(serial, x, y):
	rack_id = x + 10
	power_level = rack_id * y
	power_level += serial
	power_level *= rack_id
	digit = int(str(power_level)[-3])
	return digit - 5

def day11(serial):
	grid = [[0 for _ in range(301)] for _ in range(301)]
	for x in range(1, 301):
		for y in range(1, 301):
			grid[y][x] = calculate_power_level(serial, x, y)
	
	max_x, max_y = 0, 0
	best_size = 0
	max_power_level = float('-inf')
	for size in range(1, 301):
		power_level = 0
		for y in range(1,301):
			for x in range(1, 301):
				if 0 <= x <= 301 - size and 0 <= y <= 301 - size:
					if power_at_corner > max_power_level:
						max_power_level = power_at_corner
						max_x, max_y = x, y
					power_at_corner += 
	return (max_x, max_y)

print(day11(18))	
print(day11(42))	
#print(day11(2187))	
	
