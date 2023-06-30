from unittest import TestCase

from ds.tree.binary_tree import BinaryTree, BinaryTreeNode, BST
from ds.tree.tree import TreeNode, Tree
from ds.tree.trie import TrieNode


class TestBinaryTree(TestCase):

    def test_insert_binary_tree(self):
        tree = BinaryTree(init_value=1)
        tree.insert(2)
        tree.insert(3)
        tree.insert(4)

        self.assertEqual(tree.root.value, 1)
        self.assertEqual(tree.root.left.value, 2)
        self.assertEqual(tree.root.right.value, 3)
        self.assertEqual(tree.root.left.left.value, 4)

    def test_delete_from_binary_tree(self):
        tree = BinaryTree(init_value=1)
        tree.insert(2)
        tree.insert(3)
        tree.insert(4)

        tree.delete(value=2)

        self.assertEqual(tree.root.value, 1)
        self.assertEqual(tree.root.left.value, 4)
        self.assertEqual(tree.root.right.value, 3)
        self.assertTrue(tree.root.left.is_leaf)
        self.assertTrue(tree.root.right.is_leaf)

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

        self.assertEqual(tree.get_level_nodes(target_level=1), [tree.root])
        self.assertEqual(tree.get_level_nodes(target_level=2), [node_2, node_3])
        self.assertEqual(tree.get_level_nodes(target_level=3), [node_4])

    def test_bfs(self):
        tree = BinaryTree(init_value=1)
        node_2 = tree.insert(2)
        node_3 = tree.insert(3)
        node_4 = tree.insert(4)

        self.assertEqual(tree.bfs(), [tree.root, node_2, node_3, node_4])

    def test_in_order(self):
        tree = BinaryTree(init_value=1)
        node_2 = tree.insert(2)
        node_3 = tree.insert(3)
        node_4 = tree.insert(4)

        self.assertEqual(tree.in_order(), [node_4, node_2, tree.root, node_3])

    def test_pre_order(self):
        tree = BinaryTree(init_value=1)
        node_2 = tree.insert(2)
        node_3 = tree.insert(3)
        node_4 = tree.insert(4)

        self.assertEqual(tree.pre_order(), [tree.root, node_2, node_4, node_3])

    def test_post_order(self):
        tree = BinaryTree(init_value=1)
        node_2 = tree.insert(2)
        node_3 = tree.insert(3)
        node_4 = tree.insert(4)

        self.assertEqual(tree.post_order(), [node_4, node_2, node_3, tree.root])

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


class TestBST(TestCase):

    def test_bst_search_with_existed_value_return_node(self):
        tree = BST(init_value=2)
        tree.root.left = BinaryTreeNode(value=1)
        tree.root.right = BinaryTreeNode(value=3)

        self.assertEqual(tree.search(value=3), tree.root.right)

    def test_bst_search_with_not_existed_value_return_none(self):
        tree = BST(init_value=2)
        tree.root.left = BinaryTreeNode(value=1)
        tree.root.right = BinaryTreeNode(value=3)

        self.assertIsNone(tree.search(value=4))

    def test_bst_insert(self):
        tree = BST(init_value=3)
        node_1 = tree.insert(1)
        node_2 = tree.insert(2)
        node_4 = tree.insert(4)
        node_5 = tree.insert(5)

        self.assertEqual(tree.root.left, node_1)
        self.assertEqual(tree.root.left.right, node_2)
        self.assertEqual(tree.root.right, node_4)
        self.assertEqual(tree.root.right.right, node_5)

    def test_bst_insert_with_not_existed_value_return_new_node(self):
        tree = BST(init_value=2)
        tree.root.left = BinaryTreeNode(value=1)
        tree.root.right = BinaryTreeNode(value=3)

        new_node = tree.insert(4)
        self.assertEqual(new_node.value, 4)
        self.assertTrue(new_node.is_leaf)
        self.assertEqual(new_node.parent.value, 3)

    def test_bst_insert_with_existed_value_return_none(self):
        tree = BST(init_value=2)
        tree.root.left = BinaryTreeNode(value=1)
        tree.root.right = BinaryTreeNode(value=3)

        new_node = tree.insert(3)
        self.assertIsNone(new_node)

    def test_bst_delete_with_not_existed_value_return_false(self):
        tree = BST(init_value=2)
        tree.root.left = BinaryTreeNode(value=1)
        tree.root.right = BinaryTreeNode(value=3)

        new_node = tree.delete(4)
        self.assertFalse(new_node)

    def test_bst_delete_with_existed_value_with_single_left_child_return_true(self):
        tree = BST(init_value=3)
        tree.root.left = BinaryTreeNode(value=2)
        tree.root.left.left = BinaryTreeNode(value=1)
        tree.root.right = BinaryTreeNode(value=4)

        new_node = tree.delete(2)
        self.assertTrue(new_node)
        self.assertIsNone(tree.root.left.left)
        self.assertEqual(tree.root.value, 3)
        self.assertEqual(tree.root.left.value, 1)

    def test_bst_delete_with_existed_value_with_single_right_child_return_true(self):
        tree = BST(init_value=2)
        tree.root.left = BinaryTreeNode(value=1)
        tree.root.right = BinaryTreeNode(value=3)
        tree.root.right.right = BinaryTreeNode(value=4)

        new_node = tree.delete(3)
        self.assertTrue(new_node)
        self.assertIsNone(tree.root.right.right)
        self.assertEqual(tree.root.right.value, 4)
        self.assertEqual(tree.root.value, 2)
        self.assertEqual(tree.root.left.value, 1)

    def test_bst_delete_with_existed_value_without_child_return_true(self):
        tree = BST(init_value=2)
        tree.root.left = BinaryTreeNode(value=1)
        tree.root.right = BinaryTreeNode(value=3)

        new_node = tree.delete(3)
        self.assertTrue(new_node)
        self.assertIsNone(tree.root.right)
        self.assertEqual(tree.root.value, 2)
        self.assertEqual(tree.root.left.value, 1)

    def test_bst_delete_with_existed_value_child_return_true(self):
        tree = BST(init_value=2)
        tree.root.left = BinaryTreeNode(value=1)
        tree.root.right = BinaryTreeNode(value=4)
        tree.root.right.left = BinaryTreeNode(value=3)
        tree.root.right.right = BinaryTreeNode(value=7)
        tree.root.right.right.left = BinaryTreeNode(value=6)
        tree.root.right.right.right = BinaryTreeNode(value=8)

        new_node = tree.delete(4)
        self.assertTrue(new_node)
        self.assertIsNone(tree.root.right.right.left)
        self.assertEqual(tree.root.right.value, 6)
        self.assertEqual(tree.root.right.left.value, 3)
        self.assertEqual(tree.root.right.right.value, 7)
        self.assertEqual(tree.root.right.right.right.value, 8)

    def test_height_node(self):
        tree = BST(init_value=1)
        node_2 = tree.insert(2)
        node_3 = tree.insert(3)
        node_4 = tree.insert(4)

        self.assertEqual(node_2.height, 3)
        self.assertEqual(node_3.height, 2)
        self.assertEqual(node_4.height, 1)

    def test_get_level_nodes(self):
        tree = BST(init_value=3)
        node_2 = tree.insert(2)
        node_1 = tree.insert(1)
        node_4 = tree.insert(4)

        self.assertEqual(tree.get_level_nodes(target_level=1), [tree.root])
        self.assertEqual(tree.get_level_nodes(target_level=2), [node_2, node_4])
        self.assertEqual(tree.get_level_nodes(target_level=3), [node_1])

    def test_bfs(self):
        tree = BST(init_value=2)
        node_2 = tree.insert(1)
        node_3 = tree.insert(3)
        node_4 = tree.insert(4)

        self.assertEqual(tree.bfs(), [tree.root, node_2, node_3, node_4])

    def test_in_order(self):
        tree = BST(init_value=3)
        node_2 = tree.insert(2)
        node_1 = tree.insert(1)
        node_4 = tree.insert(4)

        self.assertEqual(tree.in_order(), [node_1, node_2, tree.root, node_4])

    def test_pre_order(self):
        tree = BST(init_value=3)
        node_2 = tree.insert(2)
        node_1 = tree.insert(1)
        node_4 = tree.insert(4)

        self.assertEqual(tree.pre_order(), [tree.root, node_2, node_1, node_4])

    def test_post_order(self):
        tree = BST(init_value=3)
        node_2 = tree.insert(2)
        node_1 = tree.insert(1)
        node_4 = tree.insert(4)

        self.assertEqual(tree.post_order(), [node_1, node_2, node_4, tree.root])

    def test_str_bst(self):
        tree = BST(init_value=3)
        tree.insert(1)
        tree.insert(2)
        tree.insert(4)
        tree.insert(5)

        self.assertEqual(
            str(tree),
            "   3   \n"
            " 1   4 \n"
            "  2   5"
        )


class TestTreeNode(TestCase):

    def test_tree_node_with_parent(self):
        root = TreeNode(value=1)
        node_2 = TreeNode(value=2, parent=root)

        self.assertEqual(node_2.parent, root)
        self.assertEqual(root.children, [node_2])

    def test_tree_node_add_child(self):
        root = TreeNode(value=1)
        root.add_child(2)
        root.add_child(3)

        self.assertEqual(root.children, [TreeNode(value=2), TreeNode(value=3)])

    def test_tree_node_remove_child(self):
        root = TreeNode(value=1)
        root.children = [TreeNode(value=2, parent=root), TreeNode(value=3, parent=root)]
        root.remove_child(2)

        self.assertEqual(root.children, [TreeNode(value=3)])

    def test_tree_node_equality(self):
        root = TreeNode(value=1)
        node_1 = TreeNode(value=2, parent=root)
        node_2 = TreeNode(value=2, parent=root)

        self.assertEqual(node_1, node_2)

    def test_tree_node_height(self):
        root = TreeNode(value=1)
        node_2 = root.add_child(2)
        root.add_child(3)
        node_4 = node_2.add_child(4)
        node_4.add_child(5)

        self.assertEqual(root.height, 4)
        self.assertEqual(root.children[0].height, 3)
        self.assertEqual(root.children[0].children[0].height, 2)
        self.assertEqual(root.children[0].children[0].children[0].height, 1)

    def test_tree_node_str(self):
        node_1 = TreeNode(value=1)
        TreeNode(value=2, parent=node_1)
        TreeNode(value=3, parent=node_1)

        self.assertEqual(
            str(node_1),
            '1\n\t2\n\t3\n'
        )


class TestTree(TestCase):

    def test_tree_bfs(self):
        tree = Tree(init_value=1)
        node_2 = tree.root.add_child(2)
        node_3 = tree.root.add_child(3)
        node_4 = node_2.add_child(4)
        node_5 = node_2.add_child(5)
        node_6 = node_3.add_child(6)
        node_7 = node_3.add_child(7)

        self.assertEqual(
            tree.bfs(),
            [tree.root, node_2, node_3, node_4, node_5, node_6, node_7])

    def test_tree_dfs(self):
        tree = Tree(init_value=1)
        node_2 = tree.root.add_child(2)
        node_3 = tree.root.add_child(3)
        node_4 = node_2.add_child(4)
        node_5 = node_2.add_child(5)
        node_6 = node_2.add_child(6)
        node_7 = node_3.add_child(7)
        node_8 = node_3.add_child(8)
        node_9 = node_3.add_child(9)

        self.assertEqual(
            tree.dfs(),
            [tree.root, node_2, node_4, node_5, node_6, node_3, node_7, node_8, node_9])

    def test_tree_get_level_nodes(self):
        tree = Tree(init_value=1)
        node_2 = tree.root.add_child(2)
        node_3 = tree.root.add_child(3)
        node_4 = node_2.add_child(4)
        node_5 = node_2.add_child(5)
        node_6 = node_2.add_child(6)
        node_7 = node_3.add_child(7)
        node_8 = node_3.add_child(8)
        node_9 = node_3.add_child(9)

        self.assertEqual(
            tree.get_level_nodes(3),
            [node_4, node_5, node_6, node_7, node_8, node_9]
        )

    def test_tree_str(self):
        tree = Tree(init_value=1)
        tree.root.add_child(2)
        tree.root.add_child(3)

        self.assertEqual(
            str(tree),
            "1\n\t2\n\t3\n"
        )

    def test_tree_str_2(self):
        tree = Tree(init_value=1)
        node_2 = tree.root.add_child(2)
        node_3 = tree.root.add_child(3)
        node_2.add_child(4)
        node_2.add_child(5)
        node_2.add_child(6)
        node_3.add_child(7)
        node_3.add_child(8)
        node_3.add_child(9)

        self.assertEqual(
            str(tree),
            '1\n\t2\n\t\t4\n\t\t5\n\t\t6\n\t3\n\t\t7\n\t\t8\n\t\t9\n'
        )


class TestTrieNode(TestCase):

    def test_trie_node_with_parent(self):
        root = TrieNode(value="a")
        node_2 = TrieNode(value="m", parent=root)

        self.assertEqual(node_2.parent, root)
        self.assertEqual(root.children, {node_2})

    def test_trie_node_add_child(self):
        root = TrieNode(value="a")
        root.add_child("m")
        root.add_child("i")
        root.add_child("i")

        self.assertEqual(root.children, {TrieNode(value="m"), TrieNode(value="i")})

    def test_trie_node_remove_child(self):
        root = TrieNode(value="a")
        root.add_child("m")
        root.add_child("i")
        root.remove_child("i")

        self.assertEqual(root.children, {TrieNode(value="m")})

    def test_trie_node_equality(self):
        root = TrieNode(value="a")
        node_1 = TrieNode(value="i", parent=root)
        node_2 = TrieNode(value="i", parent=root)

        self.assertEqual(node_1, node_2)
