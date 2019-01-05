class Coordinate(object):
	def __init__(self):
		self.x = 0
		self.y = 0
		self.z = 0

def cube_distance(a, b):
    return (abs(a.x - b.x) + abs(a.y - b.y) + abs(a.z - b.z)) / 2

path = open('input/input.txt','r').readline().split(',')
#path = 'se,sw,se,sw,sw'.split(',')
origin = Coordinate()
location = Coordinate()
max_distance = 0

for direction in path:
	if direction == 'n':
		location.y += 1
		location.z -= 1
	elif direction == 'nw':
		location.y += 1
		location.x -= 1
	elif direction == 'ne':
		location.x += 1
		location.z -= 1
	elif direction == 's':
		location.y -= 1
		location.z += 1
	elif direction == 'se':
		location.x += 1
		location.y -= 1
	elif direction == 'sw':
		location.x -= 1
		location.z += 1
	else:
		print('Invalid location')

	distance = cube_distance(origin, location)
	if distance > max_distance:
		max_distance = distance

print(cube_distance(origin, location))
print(max_distance)