"""Sorted insert"""
class Node(object):
    """Node class"""
    def __init__(self, data):
        self.data = data
        self.next = None

def sorted_insert(head: Node, data: int) -> Node:
    """Insert a new node into a sorted list"""
    our_node = Node(data)
    if head is None or data <= head.data:
        our_node.next = head
        return our_node
    current = head
    while current.next is not None and current.next.data <= data:
        current = current.next
    our_node.next = current.next
    current.next = our_node
    return head
