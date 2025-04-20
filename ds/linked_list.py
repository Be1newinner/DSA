
# Linked List => A LInear Data Structure where each node points to its next node.

# Single Linked List => Here Each node has data and next value reference

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None 
        
class SingleLinkedList:
    def __init__(self):
        self.head = None
        
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node
        
    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data, end=" => ")
            curr = curr.next
        print("None")

def reverse_single_list(head):
    prev = None
    curr = head
    while curr:                     
        nxt = curr.next             
        curr.next = prev            
        prev = curr                 
        curr = nxt        

# Flyod or (Tortorise and hare algorithm) 
def check_single_list_cycle(head):
    fast = slow = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return True
    
    return False    

     
# Usage
ls = SingleLinkedList()
ls.insert_at_end("Hi")
ls.insert_at_end("Bye")
ls.insert_at_end("Nye")
ls.insert_at_end("Dye")
ls.insert_at_end("Fye")

ls.print_list()