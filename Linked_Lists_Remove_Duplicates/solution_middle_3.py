"""Remove duplicates"""
class Node(object):
    """Node class"""
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head: Node) -> Node:
    """Removing nodes with the same data"""
    if head is None:
        return None
    curr = head
    while curr and curr.next:
        if curr.data == curr.next.data:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return head
