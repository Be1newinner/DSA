from collections import deque

tree = deque()
tree.append(5)
tree.append(6)
tree.append(1)
tree.append(3)
tree.append(9)

data = [x for x in tree]  

print(data)