"""Alternating split"""
class Node(object):
    """Node class"""
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Context(object):
    """Context class"""
    def __init__(self, first, second):
        self.first = first
        self.second = second

def alternating_split(head: Node) -> Context:
    """Takes one list and divides up its nodes to make two smaller lists"""
    if head is None or head.next is None:
        raise Exception("Head shouldn't be None")
    first = first_end = None
    second = second_end = None
    flag = True
    curr = head
    while curr:
        new = curr.next
        curr.next = None
        if flag:
            if first == None:
                first = curr
                first_end = curr
            else:
                first_end.next = curr
                first_end = curr
        else:
            if second is None:
                second = curr
                second_end = curr
            else:
                second_end.next = curr
                second_end = curr
        curr = new
        flag = not flag
    return Context(first, second)
