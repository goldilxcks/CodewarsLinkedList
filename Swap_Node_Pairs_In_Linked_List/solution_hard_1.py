"""Swapping nodes function"""
class Node(object):
    """Node class"""
    def __init__(self, data):
        self.data = data
        self.next = None

def swap_pairs(head: Node) -> Node:
    """Swaps each pair of nodes in the list, \
then returns the head node of the list"""
    probe = Node(0)
    probe.next = head
    last = probe
    while last.next and last.next.next:
        first = last.next
        second = first.next
        last.next = second
        first.next = second.next
        second.next = first
        last = first
    return probe.next
