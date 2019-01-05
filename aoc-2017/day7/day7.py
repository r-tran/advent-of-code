data = open('input/input.txt', 'r').readlines()
nodes = [line.split()[0] for line in data]
leaves = [line.split()[0] for line in data if "->" not in line]

adjacents = {}
for line in data:
	if "->" in line:
		adjacents[line.split()[0]] = line.split(' -> ')[1].strip().split(', ')

node_weights = {}
for line in data:
	node_weights[line.split()[0]] = int(line.split()[1].strip('(').strip(')'))


def calculate_weighted_edges(node):
	if node in leaves: 
		return node_weights[node]
	else:
		total_weight = 0
		for child in adjacents[node]:
			total_weight += calculate_weighted_edges(child)
		return node_weights[node] + total_weight

def get_heaviest_node(root):
	weights = []
	heaviest_node = None
	heaviest_weight = 0
	for child in adjacents[root]:
		weight = calculate_weighted_edges(child)
		if weight > heaviest_weight:
			heaviest_weight = weight
			heaviest_node = child
		weights.append(weight)
	
	if min(weights) == max(weights):
		return root

	return get_heaviest_node(heaviest_node)

#Part One 
root = nodes
for node in adjacents:
	for neighbor in adjacents[node]:
		root.remove(neighbor)

if len(root) != 1:
	print('ERROR: Multiple roots found!')

#Part Two 
root = root[0]
print('Root is {}'.format(root))

heaviest = get_heaviest_node(root)
print('Heaviest node is {}'.format(heaviest))

weights = [calculate_weighted_edges(child) for child in adjacents[root]]
print('Adjusted weight {}'.format(node_weights[heaviest] - (max(weights) - min(weights))))
