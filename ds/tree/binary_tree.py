from collections import deque
from typing import Any, NoReturn

from ds.tree import TreeNode, BaseTree


class BinaryTree(BaseTree):

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
            return False

        deleting_node.value = last_node.value

        if last_node.parent.left == last_node:
            last_node.parent.left = None
        else:
            last_node.parent.right = None

        return True
