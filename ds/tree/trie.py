from collections import UserDict


class TrieNode:

    def __init__(self, value: str, parent=None, is_end_of_word: bool = False):
        self.value = value
        self.parent = parent
        self.is_end_of_word = is_end_of_word

        if parent:
            parent.children.add(self)

        self.children = TrieNodeChildren()

    @property
    def height(self):
        if self.is_leaf:
            return 1

        return max([node.height for node in self.children.values()]) + 1

    @property
    def is_leaf(self) -> bool:
        return not bool(self.children)

    def add_child(self, value: str):
        new_node = TrieNode(value=value)
        new_node.parent = self
        self.children[value] = new_node
        return new_node

    def remove_child(self, value: str):
        remove_node = TrieNode(value=value)
        remove_node.parent = self
        self.children.pop(value)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.value == other.value

        return self.value == other

    def __hash__(self):
        return hash(self.value)

    def __str__(self):
        return f"Node {self.value}"

    def __repr__(self):
        return self.__str__()


class TrieNodeChildren(UserDict):

    def __getattr__(self, item):
        return self.data.get(item)

    def __eq__(self, other):
        return self.data == other

    def add(self, node: TrieNode):
        self.data[node.value] = node


class Trie:

    def __init__(self, init_value=None):
        self.root = TrieNode(value=init_value)

    def insert(self, word: str):
        current = self.root
        for char in word:
            new_node = current.add_child(char)
            current = new_node

        current.is_end_of_word = True

    def search(self, word: str) -> bool:
        current = self.root
        for char in word:
            if char not in current.children:
                return False

            current = current.children[char]

        if not current.is_end_of_word:
            return False

        return True
