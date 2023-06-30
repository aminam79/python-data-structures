import abc
from typing import Any, NoReturn
from collections import deque


class BinaryTreeNode:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self._left = left
        self._right = right

        self.parent: BinaryTreeNode | None = None

        if left:
            self._left.parent = self
        if right:
            self._right.parent = self

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, value):
        self._left = value
        if value is not None:
            self._left.parent = self

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, value):
        self._right = value
        if value is not None:
            self._right.parent = self

    @property
    def is_leaf(self):
        return not self.left and not self.right

    @property
    def height(self):
        if self.is_leaf:
            return 1

        left_height = self.left.height if self.left else 0
        right_height = self.right.height if self.right else 0

        return max(left_height, right_height) + 1

    def __str__(self):
        return f"Node {self.value}"

    def __repr__(self):
        return self.__str__()


class BaseBinaryTree(abc.ABC):

    def __init__(self, init_value):
        self.root = BinaryTreeNode(value=init_value)

    @property
    def height(self) -> int:
        return self.root.height

    @abc.abstractmethod
    def insert(self, value) -> BinaryTreeNode:
        raise NotImplementedError

    @abc.abstractmethod
    def delete(self, value) -> bool:
        raise NotImplementedError

    def get_level_nodes(self, target_level: int) -> list[BinaryTreeNode]:
        q = deque([(self.root, 1)])
        result = []

        while q:
            node, level = q.popleft()

            if level == target_level:
                result.append(node)
            elif level > target_level:
                break

            if node.left:
                q.append((node.left, level + 1))

            if node.right:
                q.append((node.right, level + 1))

        return result

    def bfs(self) -> list[BinaryTreeNode]:
        q = deque([self.root])
        result = []

        while q:
            node = q.popleft()
            result.append(node)

            if node.left:
                q.append(node.left)

            if node.right:
                q.append(node.right)

        return result

    def in_order(self) -> list[BinaryTreeNode]:
        ret = []

        def _dfs(node: BinaryTreeNode):
            if not node:
                return

            _dfs(node.left)
            ret.append(node)
            _dfs(node.right)

        _dfs(self.root)

        return ret

    def pre_order(self) -> list[BinaryTreeNode]:
        ret = []

        def _dfs(node: BinaryTreeNode):
            if not node:
                return

            ret.append(node)
            _dfs(node.left)
            _dfs(node.right)

        _dfs(self.root)

        return ret

    def post_order(self) -> list[BinaryTreeNode]:
        ret = []

        def _dfs(node: BinaryTreeNode):
            if not node:
                return

            _dfs(node.left)
            _dfs(node.right)
            ret.append(node)

        _dfs(self.root)

        return ret

    def __str__(self):
        height = self.height - 1

        def gen_matrix(node: BinaryTreeNode, m: list[list], i: int, j: int):
            if not node:
                return

            m[i][j] = str(node.value)
            gen_matrix(node.left, m, i+1, j-(2 ** (height-i-1)))
            gen_matrix(node.right, m, i+1, j+(2 ** (height-i-1)))

        col = 2 ** (height+1) - 1
        matrix = [[" " for _ in range(col)] for __ in range(height + 1)]
        gen_matrix(self.root, matrix, 0, (col - 1) // 2)

        return "\n".join(["".join(r) for r in matrix])

    def __repr__(self):
        return f"Binary tree with {self.root} root"


class BinaryTree(BaseBinaryTree):

    def insert(self, value: Any) -> BinaryTreeNode:
        q = deque([self.root])
        new_node = BinaryTreeNode(value=value)

        while q:
            node = q.popleft()
            if not node.left:
                node.left = new_node
                node.left.parent = node
                return new_node
            else:
                q.append(node.left)

            if not node.right:
                node.right = new_node
                node.right.parent = node
                return new_node
            else:
                q.append(node.right)

    def delete(self, value) -> NoReturn:
        q = deque([self.root])

        deleting_node = None
        last_node = None

        while q:
            node = q.popleft()
            if node.value == value:
                deleting_node = node

            if node.is_leaf:
                last_node = node

            if node.left:
                q.append(node.left)

            if node.right:
                q.append(node.right)

        if not deleting_node:
            return False

        deleting_node.value = last_node.value

        if last_node.parent.left == last_node:
            last_node.parent.left = None
        else:
            last_node.parent.right = None

        return True


class BST(BaseBinaryTree):

    def insert(self, value) -> BinaryTreeNode | None:
        created_node = None

        def _insert(node: BinaryTreeNode):
            if not node:
                new_node = BinaryTreeNode(value=value)
                nonlocal created_node
                created_node = new_node
                return new_node

            if node.value == value:
                return node

            if node.value < value:
                node.right = _insert(node.right)
            else:
                node.left = _insert(node.left)

            return node

        _insert(self.root)
        return created_node

    def delete(self, value) -> bool:

        found = False

        def _delete(node: BinaryTreeNode):
            if not node:
                return node

            if node.value == value:
                nonlocal found
                found = True

                if node.is_leaf:
                    return None

                if node.left and not node.right:
                    return node.left

                if node.right and not node.left:
                    return node.right

                else:
                    parent = node
                    current = parent.right
                    while current.left:
                        parent = current
                        current = current.left

                    if parent != node:
                        parent.left = current.right
                    else:
                        parent.right = current.right

                    node.value = current.value

                    return node

            if node.value < value:
                node.right = _delete(node.right)
            else:
                node.left = _delete(node.left)

            return node

        _delete(self.root)
        return found

    def search(self, value) -> BinaryTreeNode | None:
        def _search(node: BinaryTreeNode):
            if not node or node.value == value:
                return node

            if node.value < value:
                return _search(node.right)

            return _search(node.left)

        return _search(self.root)
