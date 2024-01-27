import copy


class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        """
        Print list
        :return:
        """
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.length = 1
        else:

            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        tail = self.tail

        if self.length > 1:
            self.tail = self.tail.prev
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None

        tail.prev = None
        return tail

    def prepend(self):
        pass

    def pop_first(self):
        pass


if __name__ == "__main__":
    ll = DoublyLinkedList(1)
    ll.append(2)
    ll.append(3)
    ll.print_list()
