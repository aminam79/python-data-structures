from unittest import TestCase

from ds.tree.binary_tree import BinaryTree


class TestBinaryTree(TestCase):

    def test_insert_binary_tree(self):
        tree = BinaryTree(init_value=1)
        tree.insert(2)
        tree.insert(3)
        tree.insert(4)

        self.assertEqual(tree.head.value, 1)
        self.assertEqual(tree.head.left.value, 2)
        self.assertEqual(tree.head.right.value, 3)
        self.assertEqual(tree.head.left.left.value, 4)

    def test_delete_from_binary_tree(self):
        tree = BinaryTree(init_value=1)
        tree.insert(2)
        tree.insert(3)
        tree.insert(4)

        tree.delete(value=2)

        self.assertEqual(tree.head.value, 1)
        self.assertEqual(tree.head.left.value, 4)
        self.assertEqual(tree.head.right.value, 3)
        self.assertTrue(tree.head.left.is_leaf)
        self.assertTrue(tree.head.right.is_leaf)

    def test_height(self):
        tree = BinaryTree(init_value=1)
        tree.insert(2)
        tree.insert(3)
        tree.insert(4)

        self.assertEqual(tree.height, 3)

    def test_height_node(self):
        tree = BinaryTree(init_value=1)
        node_2 = tree.insert(2)
        node_3 = tree.insert(3)
        node_4 = tree.insert(4)

        self.assertEqual(node_2.height, 2)
        self.assertEqual(node_3.height, 1)
        self.assertEqual(node_4.height, 1)

    def test_get_level_nodes(self):
        tree = BinaryTree(init_value=1)
        node_2 = tree.insert(2)
        node_3 = tree.insert(3)
        node_4 = tree.insert(4)

        self.assertEqual(tree.get_level_nodes(target_level=1), [tree.head])
        self.assertEqual(tree.get_level_nodes(target_level=2), [node_2, node_3])
        self.assertEqual(tree.get_level_nodes(target_level=3), [node_4])

    def test_bfs(self):
        tree = BinaryTree(init_value=1)
        node_2 = tree.insert(2)
        node_3 = tree.insert(3)
        node_4 = tree.insert(4)

        self.assertEqual(tree.bfs(), [tree.head, node_2, node_3, node_4])

    def test_str_binary_tree(self):
        tree = BinaryTree(init_value=1)
        tree.insert(2)
        tree.insert(3)
        tree.insert(4)
        tree.insert(5)

        self.assertEqual(
            str(tree),
            "   1   \n"
            " 2   3 \n"
            "4 5    "
        )

    def test_str_binary_tree_1(self):
        tree = BinaryTree(init_value=1)
        tree.insert(2)
        tree.insert(3)
        tree.insert(4)
        tree.insert(5)
        tree.insert(6)
        tree.insert(7)

        self.assertEqual(
            str(tree),
            "   1   \n"
            " 2   3 \n"
            "4 5 6 7"
        )
