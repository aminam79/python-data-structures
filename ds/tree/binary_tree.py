from collections import deque
from typing import Any, NoReturn

from ds.tree import TreeNode


class BinaryTree:

    def __init__(self, init_value: Any | None):
        self.root = TreeNode(value=init_value)

    @property
    def height(self) -> int:
        return self.root.height

    def insert(self, value: Any) -> TreeNode:
        q = deque([self.root])
        new_node = TreeNode(value=value)

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
            return

        deleting_node.value = last_node.value

        if last_node.parent.left == last_node:
            last_node.parent.left = None
        else:
            last_node.parent.right = None

    def get_level_nodes(self, target_level: int) -> list[TreeNode]:
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

    def bfs(self) -> list[TreeNode]:
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

    def in_order(self) -> list[TreeNode]:
        ret = []

        def _dfs(node: TreeNode):
            if not node:
                return

            _dfs(node.left)
            ret.append(node)
            _dfs(node.right)

        _dfs(self.root)

        return ret

    def pre_order(self) -> list[TreeNode]:
        ret = []

        def _dfs(node: TreeNode):
            if not node:
                return

            ret.append(node)
            _dfs(node.left)
            _dfs(node.right)

        _dfs(self.root)

        return ret

    def post_order(self) -> list[TreeNode]:
        ret = []

        def _dfs(node: TreeNode):
            if not node:
                return

            _dfs(node.left)
            _dfs(node.right)
            ret.append(node)

        _dfs(self.root)

        return ret

    def __str__(self):
        height = self.height - 1

        def gen_matrix(node: TreeNode, m: list[list], i: int, j: int):
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
