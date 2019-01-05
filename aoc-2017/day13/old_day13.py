class Layer(object):
	def __init__(self, nrange):
		self.range = nrange
		self.current = 1
		self.step = 1

	def move(self):
		if self.current == 1:
			self.step = 1
		if self.current == self.range:
			self.step = -1

		self.current += self.step

def print_state(active_layers):
	for layer in active_layers:
		print('Layer: {}, Curr: {}, Range: {}'.format(layer, active_layers[layer].current, active_layers[layer].range))

def step_all_active_layers(active_layers):
	for layer in active_layers:
		active_layers[layer].move()

def get_captured_layers(delay):
	active_layers = {}
	for layer in layers:
		active_layers[layer] = Layer(layers[layer])

	layer_captured = []
	for j in range(delay):
		step_all_active_layers(active_layers)
	#print_state()
	for i in range(max(layers.keys()) + 1):
		if i in layers and active_layers[i].current == 1:
			layer_captured.append(i)
		step_all_active_layers(active_layers)
	return layer_captured

def score_captured_layers(captured):
	score = 0
	for layer in captured:
		score += active_layers[layer].range * layer
	return score

data = open('input/input.txt', 'r').readlines()
layers = {}
for line in data:
	layers[int(line.split(': ')[0])] = int(line.split(': ')[1])

# Part One
#captured = get_captured_layers(0)
#print(score_captured_layers(captured))

#Part Two
time = 0
while len(get_captured_layers(time)) != 0:	
    time += 1
    print(time)

print(time)
