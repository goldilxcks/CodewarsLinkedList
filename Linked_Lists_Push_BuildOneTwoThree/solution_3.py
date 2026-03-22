"""
Push and build 1 2 3 function
"""
class Node:
    """Node class"""
    def __init__(self, data):
        self.data = data
        self.next = None

def push(head, data) -> Node:
    """Adding the Node new as the head """
    final_nde = Node(data)
    final_nde.next = head
    return final_nde

def build_one_two_three() -> Node:
    """create and return a linked list with three node"""
    head = None
    for i in range(3, 0, -1):
        head = push(head, i)
    return head
