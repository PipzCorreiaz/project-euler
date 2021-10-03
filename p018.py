import math

triangle2 = [
[3],
[7, 4],
[2, 4, 6],
[8, 5, 9, 3]]

triangle = [
[75],
[95, 64],
[17, 47, 82],
[18, 35, 87, 10],
[20, 04, 82, 47, 65],
[19, 01, 23, 75, 03, 34],
[88, 02, 77, 73, 07, 63, 67],
[99, 65, 04, 28, 06, 16, 70, 92],
[41, 41, 26, 56, 83, 40, 80, 70, 33],
[41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
[53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
[70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
[91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
[63, 66, 04, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
[04, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]]



class Node:
	def __init__(self, value):
		self.value = value
		self.children = []


nodes = []

i = 0
for line in triangle:
	nodes_line = []
	j = 0
	for num in line:
		n = Node(num)
		nodes_line.append(n)
		if i > 0 and j == 0:
			parent = nodes[i - 1][j]
			parent.children.append(n)
		elif i > 0 and j == i:
			parent = nodes[i - 1][j - 1]
			parent.children.append(n)
		elif i > 0 and j < i:
			parent = nodes[i - 1][j - 1]
			parent.children.append(n)
			parent = nodes[i - 1][j]
			parent.children.append(n)
		j += 1
	copy = []
	for k in nodes_line:
		copy.append(k)
	nodes.append(copy)
	i += 1



max_route = 0

def dfs(node):
	def aux(node, route_val):
		route_val += node.value
		if node.children == []:
			return route_val
		else:
			val1 = aux(node.children[0], route_val)
			val2 = aux(node.children[1], route_val)
			return max(val1, val2)
	return aux(node, 0)

def dfs2(node):
	def aux(node, route_val):
		route_val += node.value
		if node.children == []:
			return route_val
		else:
			max_val = 0
			for child in node.children:
				val = aux(child, route_val)
				max_val = max(max_val, val)
			return max_val
	return aux(node, 0)


def dfs3(node):
	if node.children == []:
		return node.value
	return max(node.value + dfs3(node.children[0]), node.value + dfs3(node.children[1]))


print dfs3(nodes[0][0])





