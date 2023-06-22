from collections import deque
from typing import Any


class BinaryTreeNode:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

        self.parent: BinaryTreeNode | None = None

        if left:
            left.parent = self
        if right:
            right.parent = self

    @property
    def is_leaf(self):
        return not self.left and not self.right

    @property
    def height(self):
        if self.is_leaf:
            return 0

        left_height = self.left.height if self.left else 0
        right_height = self.right.height if self.right else 0

        return max(left_height, right_height) + 1

    def __str__(self):
        return f"Node {self.value}"

    def __repr__(self):
        return self.__str__()


class BinaryTree:

    def __init__(self, init_value: Any | None):
        self.head = BinaryTreeNode(value=init_value)

    @property
    def height(self):
        return self.head.height

    def insert(self, value):
        q = deque([self.head])
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

    def delete(self, value):
        q = deque([self.head])

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

    def get_level_nodes(self, target_level: int):
        q = deque([(self.head, 1)])
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

    def bfs(self):
        q = deque([self.head])
        result = []

        while q:
            node = q.popleft()
            result.append(node)

            if node.left:
                q.append(node.left)

            if node.right:
                q.append(node.right)

        return result

    def __str__(self):
        ret = ""
        q = [self.head]
        height_num = self.height - 1
        #
        # while q:
        #     ret += " " * 3 * height_num
        #
        #     node = q.pop(0)
        #     if not node.left:
        #         node.left = new_node
        #         return
        #     else:
        #         q.append(node.left)
        #
        #     if not node.right:
        #         node.right = new_node
        #         return
        #     else:
        #         q.append(node.right)
        #
        #     ret += current.value
        #     ret += " " * 3 * height_num
