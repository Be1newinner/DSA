from __future__ import annotations

# 2. Binary Search Tree (BST) ==============================================================================
# What: A binary tree where left.val < node.val < right.val.
# Why: Enables O(log n) search/insert/delete (if balanced).

# Must‑know operations:
# insert, search, delete
# Validate BST
# Kth smallest/largest element
# Floor/ceil, range queries

# Practice:
# LeetCode 98: Validate BST
# LeetCode 230: Kth Smallest BST
# LeetCode 450: Delete Node in a BST

class BST:
    def __init__(self, data: int):
        self.data = data
        self.left: BST = None
        self.right: BST = None
        
    def insert(self, data: int): 
        if not data:
            return
        
        if self.data == data:
            return
        
        if data < self.data:
            if self.left:
                self.left.insert(data)
            else:
                self.left = BST(data)
            
        else:
            if self.right:
                self.right.insert(data)
            else:
                self.right = BST(data)
                
    def inorder(self):
        def _inorder(root: BST):
            if root:
                _inorder(root.left)
                print(root.val)
                _inorder(root.right)
        return _inorder(self.root)
    
    def preorder(self):
        def _preorder(root: BST):
            if not root:
                return
            print(root.val)
            _preorder(root.left)
            _preorder(root.right)
        return _preorder(self.root)
    
    def search(self, val):
        def _search(node: BST, val):
            if not node:
                return False
            if val == node.val:
                return True
            elif val < node.val:
                return  _search(node.left, val)
            else:
                return _search(node.right, val)
        return _search(self.root, val)
    
    def delete(self, val):
        def _delete(node: BST, val):
            if not node:
                return False
            
            if val == node.val:
                temp = node.val
                val.next
            
            return node
            
        self.root = _delete(self.root, val)
        
bst = BST(21)
bst.insert(2)
bst.insert(4)
bst.insert(3)
bst.insert(5)
bst.insert(29)
bst.insert(11)
bst.insert(23)
bst.insert(5)
print("INSERT ENDS!")

# bst.inorder()

# print(bst.search(23))