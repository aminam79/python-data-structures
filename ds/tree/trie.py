class TrieNode:

    def __init__(self, value: str, parent=None, is_end_of_word: bool = False):
        self.value = value
        self.parent = parent
        self.is_end_of_word = is_end_of_word

        if parent:
            parent.children.add(self)

        self.children: set[TrieNode] = set()

    @property
    def height(self):
        if self.is_leaf:
            return 1

        return max([node.height for node in self.children]) + 1

    @property
    def is_leaf(self) -> bool:
        return not bool(self.children)

    def add_child(self, value: str):
        new_node = TrieNode(value=value)
        new_node.parent = self
        self.children.add(new_node)
        return new_node

    def remove_child(self, value: str):
        remove_node = TrieNode(value=value)
        remove_node.parent = self
        self.children.remove(remove_node)

    def __eq__(self, other):
        return self.value == other.value

    def __hash__(self):
        return hash(self.value)

    def __str__(self):
        return f"Node {self.value}"

    def __repr__(self):
        return self.__str__()
