import sys
lines = open(sys.argv[1],'r').readlines()
positions = []
velocities = []

for line in lines:
	positions.append(list(map(int, line.split('> ')[0][10:].split(', '))))
	velocities.append(list(map(int, line.split('> ')[1][10:-2].strip('\n').split(', '))))

def day10():
	pass
print(day10())
