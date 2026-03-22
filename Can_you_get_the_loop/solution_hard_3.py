"""Getting the loop's length"""
class Node(object):
    """Node class"""
    def __init__(self, data=None):
        self.data = data
        self.next = None

def loop_size(node: Node) -> int:
    """ Determine the length of the loop"""
    length = 1
    fast = node
    slow = node
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    probe = slow.next
    while probe != slow:
        length = length + 1
        probe = probe.next
    return length
