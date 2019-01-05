banks = [int(x) for x in open('input/input.txt', 'r').readline().split()]

def memory_reallocation(banks):
	configurations = []

	while True:
		blockdata = max(banks)
		location_index = banks.index(blockdata)
		banks[location_index] = 0

		while blockdata > 0:
			location_index = (location_index + 1) % len(banks)
			banks[location_index] += 1
			blockdata -= 1

		cycle = ''.join(str(b) for b in banks)
		if cycle in configurations:
			configurations.append(cycle)
			break

		configurations.append(cycle)

	for i in range(len(configurations) - 1):
		if configurations[i] == configurations[-1]:
			return len(configurations), len(configurations) - i - 1

print(memory_reallocation(banks))

