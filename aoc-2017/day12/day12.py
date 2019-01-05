from collections import deque

lines = open('input/input.txt','r').readlines()
nodes = [line.split(' <-> ')[0] for line in lines]
neighbors = [line.split(' <-> ')[1].strip('\n').split(', ') for line in lines]

node_map = {}
n = len(nodes)
for i in range(n):
	node_map[nodes[i]] = neighbors[i]

def find_group(start):
	programs = [start]
	to_explore = deque(node_map[start])

	while len(to_explore) > 0:
		explore = to_explore.popleft()
		for node in nodes:
			if node not in programs:
					if explore in node_map[node]:
						for item in node_map[node]:
							to_explore.append(item)
						programs.append(node)
	return programs

group_count = 0
while len(nodes) > 0:
	group = find_group(nodes[0])
	for item in group:
		nodes.remove(item)
	group_count += 1

print(group_count)
