from concept.LinkedList.Node import Node


class DllNode(Node):
    def __init__(self, val):
        super().__init__(val)
        self.prev=None

