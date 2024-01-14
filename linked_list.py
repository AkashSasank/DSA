class Node:
    """
    A Node. It has a value and a pointer to next node
    """

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    """
    A Linked list is a collection of nodes.
    There is a head node, and a tail node.
    Each node points to next node.
    Tail node points to None
    """

    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head

        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        """
        Append new item
        :param value:
        :return:
        """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
        return self, True

    def pop(self):
        """
        Pop the tail(last item)
        :return:
        """
        if self.length == 0:
            return None
        tail = self.tail
        temp = self.head
        new_tail = temp
        while temp.next:
            new_tail = temp
            temp = temp.next
        new_tail.next = None
        self.tail = new_tail
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return tail

    def prepend(self, value):
        """
        Add item to beginning
        :param value:
        :return:
        """
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return self, True

    def pop_first(self):
        """
        Remove first item
        :return:
        """
        if self.length == 0:
            return None
        first = self.head
        new_head = first.next
        self.head = new_head
        first.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return first

    def get(self, index):
        """
        Get node by index
        :param index:
        :return:
        """
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, value):
        """
        Set value of a node by index
        :param index:
        :param value:
        :return:
        """
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False


if __name__ == "__main__":
    ll = LinkedList(1)
