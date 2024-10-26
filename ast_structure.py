class Node:
    def __init__(self, node_type, left=None, right=None, value=None):
        self.type = node_type
        self.left = left
        self.right = right
        self.value = value

    def __repr__(self):
        if self.type == "operand":
            return f"Node(type='operand', value='{self.value}')"
        return f"Node(type='{self.type}', value='{self.value}', left={self.left}, right={self.right})"
