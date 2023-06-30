from ds.tree import TreeNode, BaseBinaryTree


class BST(BaseBinaryTree):

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

        found = False

        def _delete(node: TreeNode):
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

    def search(self, value) -> TreeNode | None:
        def _search(node: TreeNode):
            if not node or node.value == value:
                return node

            if node.value < value:
                return _search(node.right)

            return _search(node.left)

        return _search(self.root)
