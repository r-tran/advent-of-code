a_factor = 16807
b_factor = 48271
a = 618
b = 814
divisor = 2147483647
n = 5000000
i = 0 
count = 0

while i < n:
	while True:
		a = a * a_factor % divisor
		if a % 4 == 0:
			break
	print('A:%s' % a)
	while True:
		b = b * b_factor % divisor
		if b % 8 == 0:
			break
	print('B:%s' % b)

	if bin(a)[-16:] == bin(b)[-16:]:
		count += 1 
	
	i += 1
print(count)