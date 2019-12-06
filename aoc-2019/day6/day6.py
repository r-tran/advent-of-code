import fileinput

def construct_tree(data):
	parents = {}
	for line in data:
		parent, node = line.strip().split(')')
		parents[node] = parent
	return parents

def num_orbits(node, parents, root, memo):
	if node == root:
		return 0
	if node in memo:
		return memo[node]

	total = 0
	p  = parents[node]
	total = total + num_orbits(p, parents, root, memo) + 1
	memo[node] = total

	return total

tree = construct_tree(fileinput.input())

# part 1
total, memo = 0, {}
for node in tree:
	total += num_orbits(node, tree, 'COM', memo)
print(total)

#part 2
def get_ancestors(node, parent, ancestors=[]):
	if node == 'COM':
		return ancestors
	ancestors.append(parent[node])	
	return get_ancestors(parent[node], parent, ancestors)

def get_common_ancestor(a, b):
	for i in range(len(a)):
		for j in range(len(b)):
			if a[i] == b[j]:
				return a[i]
	return None

node_a, node_b = tree['YOU'], tree['SAN']
a = get_ancestors(node_a, tree, [])
b = get_ancestors(node_b, tree, [])

common_ancestor = get_common_ancestor(a, b)
res1 = num_orbits(node_a, tree, common_ancestor, {})
res2 = num_orbits(node_b, tree, common_ancestor, {})
print(res1 + res2)
