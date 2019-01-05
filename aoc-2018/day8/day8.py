import sys

nums = [int(num) for num in open(sys.argv[1],'r').readline().split()]

class Node:
	def __init__(self):
		self.metadata = []
		self.value = 0
		self.children = [] 

class Solution:
	def __init__(self):
		self.curr = 0
		self.nodes = []

	def build_tree(self):
		node = Node()
		n_children, n_metadata = nums[self.curr], nums[self.curr + 1]
		self.curr += 2
		for _ in range(n_children):
			child = self.build_tree()
			node.children.append(child)
		for _ in range(n_metadata):
			node.metadata.append(nums[self.curr])
			self.curr += 1
		
		if len(node.children) == 0:
			node.value = sum(node.metadata)
		else:
			for index in node.metadata:
				if 0 <= index - 1 < len(node.children):
					node.value += node.children[index - 1].value
		return node

sol = Solution()
root = sol.build_tree()
print(root.value)
