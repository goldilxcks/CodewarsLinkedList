"""Get nth node function"""

class Node(object):
    """Node class for reference"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def get_nth(node: Node, index: int) -> int:
    """Takes a linked list and an integer index and \
returns the node stored at the Nth index position"""
    probe = node
    count = 0
    while probe is not None:
        if count == index:
            return probe
        count += 1
        probe = probe.next
    raise IndexError("Index out of range")
