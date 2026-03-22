"""Recursive reverse"""
class Node(object):
    """Node class"""
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse(head: Node) -> Node:
    """Reverse a linked list"""
    if head is None or head.next is None:
        return head
    new_nodes = reverse(head.next)
    head.next.next = head
    head.next = None
    return new_nodes
