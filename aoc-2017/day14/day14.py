from day10 import knot_hash_algorithm

key = 'oundnydw'
hash_inputs = ['oundnydw' + '-' + str(i) for i in range(128)]
knot_hashes = [knot_hash_algorithm(64, input) for input in hash_inputs]
hash_bitstreams = ["{0:128b}".format(int(h, 16)).replace(' ', '0') for h in knot_hashes]
stream_grid = [list(stream) for stream in hash_bitstreams]

def count_set_bits(streams):
	count = 0
	for stream in streams:
		for bit in stream:
			if bit == '1':
				count += 1
	return count

def count_regions_in_grid(stream_grid):
	n_regions = 0
	for i in range(128):
		for j in range(128):
			if stream_grid[i][j] == '1':
				n_regions += 1
				stack = [(i, j)]
				while len(stack) > 0:
					(x, y) = stack.pop()
					stream_grid[x][y] = '0'
					#check up
					if x > 0 and stream_grid[x - 1][y] == '1':
						stack.append((x-1, y))
					#check down
					if x < 127 and stream_grid[x + 1][y] == '1':
						stack.append((x+1, y))
					#check left
					if y > 0 and stream_grid[x][y - 1] == '1':
						stack.append((x, y - 1))
					#check right
					if y < 127 and stream_grid[x][y + 1] == '1':
						stack.append((x, y + 1))
	return n_regions

print(count_set_bits(hash_bitstreams))
print(count_regions_in_grid(stream_grid))
