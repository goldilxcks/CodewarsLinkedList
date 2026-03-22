"""Parse a linked list"""
class Node():
    """Node class"""
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
def linked_list_from_string(list_repr: str) -> Node | None:
    """Returns a Node(1, Node(2)) after getting a string-like structure"""
    our_list = list_repr.split(" -> ")[:-1]
    head = None
    for nd in our_list[::-1]:
        head = Node(int(nd), head)
    return head
