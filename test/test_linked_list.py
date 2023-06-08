from unittest import TestCase

from linked_list import LinkedList


class TestLinkedList(TestCase):

    def test_add_value_to_linked_list(self):
        ll = LinkedList()
        ll.add(1)
        ll.add(2)
        self.assertEqual(ll.current.value, 2)
        self.assertEqual(ll.current.prior.value, 1)

    def test_remove_value_from_linked_list(self):
        ll = LinkedList()
        ll.add(1)
        ll.add(2)
        ll.remove()
        self.assertEqual(ll.current.value, 1)

    def test_remove_value_from_empty_linked_list(self):
        ll = LinkedList()
        ll.remove()
        self.assertIsNone(ll.current.value)

    def test_move_left_on_linked_list(self):
        ll = LinkedList()
        ll.add(1)
        ll.add(2)
        ll.move_left()
        ll.add(3)
        self.assertEqual(ll.current.value, 3)
        self.assertEqual(ll.current.next.value, 2)
        self.assertEqual(ll.current.prior.value, 1)

    def test_move_left_on_empty_linked_list(self):
        ll = LinkedList()
        ll.move_left()
        ll.move_left()
        ll.move_left()
        self.assertIsNone(ll.current.value)
        self.assertIsNone(ll.current.prior)
        self.assertIsNone(ll.current.next)
        self.assertEqual(str(ll), "|")

    def test_move_right_on_linked_list(self):
        ll = LinkedList()
        ll.add(1)
        ll.add(2)
        ll.move_left()
        ll.add(3)
        ll.move_right()
        ll.add(4)
        self.assertEqual(ll.current.value, 4)
        self.assertEqual(ll.current.prior.value, 2)
        self.assertEqual(ll.current.prior.prior.value, 3)

    def test_move_right_on_empty_linked_list(self):
        ll = LinkedList()
        ll.move_right()
        ll.move_right()
        ll.move_right()
        ll.move_right()
        self.assertIsNone(ll.current.value)
        self.assertIsNone(ll.current.prior)
        self.assertIsNone(ll.current.next)
        self.assertEqual(str(ll), "|")

    def test_str_linked_list(self):
        ll = LinkedList()
        ll.add(1)
        ll.add(2)
        ll.move_left()
        ll.add(3)
        self.assertEqual(str(ll), "13|2")
