from ds.tree import TreeNode, BaseTree


class BST(BaseTree):

    def insert(self, value) -> TreeNode | None:
        created_node = None

        def _insert(node: TreeNode):
            if not node:
                new_node = TreeNode(value=value)
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

        def _delete(node: TreeNode):
            if not node:
                return False

            if node.left and node.left.value == value:
                node.left = None
                return True

            if node.right and node.right.value == value:
                node.right = None
                return True

            if node.value < value:
                return _delete(node.right)
            else:
                return _delete(node.left)

        return _delete(self.root)

    def search(self, value) -> TreeNode | None:
        def _search(node: TreeNode):
            if not node or node.value == value:
                return node

            if node.value < value:
                return _search(node.right)

            return _search(node.left)

        return _search(self.root)
