from __future__ import annotations

class TreeNode:
    def __init__(self, data: str):
        self.data: str = data
        self.children: list[TreeNode] = []
        self.parent: TreeNode = None
    
    def add_child(self, child: TreeNode) -> None:
        child.parent = self
        self.children.append(child)   

    def print_tree(self) -> None:
        print(self.data)
        for child in self.children:
            if child.children:
                child.print_tree()
            else:
                print(child.data)

tree = TreeNode("ROOT")

electronics = TreeNode("ELECTRONICS")

laptop = TreeNode("Laptop")
laptop.add_child(TreeNode("MAC"))
laptop.add_child(TreeNode("INTEL"))
laptop.add_child(TreeNode("ACER"))

electronics.add_child(laptop)
tree.add_child(electronics)

furniture= TreeNode("FURNITURE")
tree.add_child(furniture)

toys = TreeNode("TOYS")
tree.add_child(toys)

tree.print_tree()

print("PROGRAM ENDS")