import operator

class Particle(object):
	def __init__(self, p, v, a):
		self.p = p
		self.v = v
		self.a = a

	def update_particle(self):
		self.v = tuple(map(operator.add, self.v, self.a))
		self.p = tuple(map(operator.add, self.p, self.v)) 

	def calculate_distance(self):
		return abs(self.p[0]) + abs(self.p[1]) + abs(self.p[2])

def parse_data():
	"""Parse data input to return list of tuples"""
	data = [line.strip('\n').split(', ') for line in open('input/input.txt', 'r').readlines()]
	particles = []

	for particle in data:
		p = tuple(map(int, particle[0][3:-1].split(',')))
		v = tuple(map(int, particle[1][3:-1].split(',')))
		a = tuple(map(int, particle[2][3:-1].split(',')))
		particles.append(Particle(p, v, a))
	return particles

def prune_collisions(particles):
	remaining = []
	for particle in particles:
		remaining.append(particle.p)
	remaining = set(remaining)

	prune = []
	for i in range(len(particles)):
		if particles[i].p in remaining:
			prune.append(particles[i])			
	return prune

def tick(n, particles):
	p = particles
	for i in range(n):
		for particle in p:
			particle.update_particle()
		p = prune_collisions(particles)
	
	return len(p)

def closest_particle(particles):
	closest_particle = float("inf")
	i = 0	
	s = 0
	for particle in particles:
		dist = particle.calculate_distance()
		if dist < closest_particle:
			closest_particle = dist
			s = i
		i += 1	
	return s		



points = parse_data()
print(tick(100, points))
print(closest_particle(points))


