masses = map(int, open('data.txt', 'r').readlines())

def calc_fuel(mass):
	total, fuel = 0, mass // 3 - 2
	while fuel > 0:
		total += fuel 
		fuel = fuel // 3 - 2
	return total

print(sum([calc_fuel(m) for m in masses]))
