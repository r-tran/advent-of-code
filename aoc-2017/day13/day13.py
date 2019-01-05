import time

data = open('input/input.txt', 'r').readlines()
ranges = {}
for line in data:
	ranges[int(line.split(': ')[0])] = int(line.split(': ')[1])

def captured_layers(delay):
	captured = []
	for depth in ranges:
		if (delay + depth) % (ranges[depth] * 2 - 2)  == 0:
			captured.append(depth)
	return captured

def captured_layers_early(delay):
	captured = []
	for depth in ranges:
		if (delay + depth) % (ranges[depth] * 2 - 2)  == 0:
			captured.append(depth)
			return captured
	return captured

#Part One
captured = captured_layers(0)
score = 0 
for depth in captured:
	score += depth * ranges[depth]

#Part Two
delay = 0
START = time.time()
while len(captured_layers(delay)) != 0:
	print(delay)
	delay += 1

print('Time: {}'.format(time.time() - START))
print(delay)

