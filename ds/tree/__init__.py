class TreeNode:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self._left = left
        self._right = right

        self.parent: TreeNode | None = None

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
