table = open('input/input.txt', 'r').readlines()
check_sum = 0
for row in table:
	values = [int(x) for x in row.split()]
	n = len(values)
	for i in range(n):
		for j in range(n):
			if values[i] % values[j] == 0 and i != j:
				check_sum += (values[i] // values[j])
print(check_sum)	