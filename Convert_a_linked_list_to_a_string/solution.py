"""Convert linked list to a string"""
class Node():
    """Node class"""
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
def stringify(node: Node):
    """MAkes a sting out of a linked list"""
    probe = node
    final = ""
    while probe is not None:
        final += f"{probe.data} -> "
        probe = probe.next
    final += 'None'
    return final
