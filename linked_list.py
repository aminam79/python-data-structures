class LinkedListNode:

    def __init__(self, value=None, next_=None, prior=None):
        self.value = value

        if next_:
            next_.prior = self
        self.next = next_

        if prior:
            prior.next_ = self
        self.prior = prior

    def __str__(self):
        return f"Node {self.value}"

    def __repr__(self):
        return self.__str__()


class LinkedList:

    def __init__(self):
        self.head = LinkedListNode()
        self.current = self.head

    def add(self, value):
        self.current.next = LinkedListNode(value=value, prior=self.current, next_=self.current.next)
        self.current = self.current.next

    def remove(self):
        if self.current.value is None:
            return

        self.current = self.current.prior

    def move_right(self):
        if not self.current.next:
            return

        self.current = self.current.next

    def move_left(self):
        if not self.current.prior:
            return

        self.current = self.current.prior

    def __str__(self):
        nodes = []
        current = self.head
        while current:
            if current.value is not None:
                nodes.append(str(current.value))
            if current == self.current:
                nodes.append("|")
            current = current.next

        return "".join(nodes)

    def __repr__(self):
        return self.__str__()
