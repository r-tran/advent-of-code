import fileinput

def construct_tree(data):
	parents = {}
	for line in data:
		parent, node = line.strip().split(')')
		parents[node] = parent
	return parents

def num_orbits(node, parent, root, memo):
	if node == root:
		return 0
	if node in memo:
		return memo[node]

	total = 0
	p  = parent[node]
	total = total + num_orbits(p, parent, root, memo) + 1
	memo[node] = total

	return total

def get_ancestors(node, parent, root, ancestors):
	if node == root:
		return ancestors
	ancestors.append(parent[node])	
	return get_ancestors(parent[node], parent, root, ancestors)

def get_common_ancestor(a, b):
	for i in range(len(a)):
		for j in range(len(b)):
			if a[i] == b[j]:
				return a[i]
	return None

tree = construct_tree(fileinput.input())

# part 1
total, memo = 0, {}
for node in tree:
	total += num_orbits(node, tree, 'COM', memo)
print(total)

#part 2
node_a, node_b = tree['YOU'], tree['SAN']
a = get_ancestors(node_a, tree, 'COM', [])
b = get_ancestors(node_b, tree, 'COM', [])

common_ancestor = get_common_ancestor(a, b)
res1 = num_orbits(node_a, tree, common_ancestor, {})
res2 = num_orbits(node_b, tree, common_ancestor, {})
print(res1 + res2)
