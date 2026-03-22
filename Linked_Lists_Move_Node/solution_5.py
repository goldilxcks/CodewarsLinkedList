"""Move node"""
class Node(object):
    """Node class"""
    def __init__(self, data):
        self.data = data
        self.next = None

class Context(object):
    """Context class"""
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest

def move_node(source: Node, dest: Node) -> Context:
    """Takes the node from the front of the source list and \
    moves it to the front of the destintation list \
    Returns the context."""
    our_node = source
    source = source.next
    our_node.next = dest
    dest = our_node
    return Context(source, dest)
