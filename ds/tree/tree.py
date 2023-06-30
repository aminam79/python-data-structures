from collections import deque


class TreeNode:

    def __init__(self, value, parent=None):
        self.value = value
        self.parent = parent

        if parent:
            parent.children.append(self)

        self.children: list[TreeNode] = []

    @property
    def height(self):
        if self.is_leaf:
            return 1

        return max([node.height for node in self.children]) + 1

    @property
    def is_leaf(self) -> bool:
        return not bool(self.children)

    def add_child(self, value):
        new_node = TreeNode(value=value)
        new_node.parent = self
        self.children.append(new_node)
        return new_node

    def remove_child(self, value):
        remove_node = TreeNode(value=value)
        remove_node.parent = self
        self.children.remove(remove_node)

    def __eq__(self, other):
        return self.value == other.value

    def __repr__(self):
        return f"Node {self.value}"

    def __str__(self, level=0):
        ret = "\t" * level + str(self.value) + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)

        return ret


class Tree:

    def __init__(self, init_value=None):
        self.root = TreeNode(value=init_value)

    @property
    def height(self):
        return self.root.height

    def bfs(self) -> list[TreeNode]:
        res = []

        q = deque([self.root])

        while q:
            node = q.popleft()
            res.append(node)
            if not node.is_leaf:
                q.extend(node.children)

        return res

    def dfs(self) -> list[TreeNode]:
        res = []

        def _dfs(node: TreeNode):
            res.append(node)
            for node in node.children:
                _dfs(node)

        _dfs(self.root)
        return res

    def get_level_nodes(self, target_level: int) -> list[TreeNode]:
        res = []

        q = deque([(self.root, 1)])

        while q:
            node, level = q.popleft()

            if level == target_level:
                res.append(node)
            elif level > target_level:
                break

            if not node.is_leaf:
                q.extend([(child, level + 1) for child in node.children])

        return res

    def __str__(self):
        return str(self.root)
