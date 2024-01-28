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
        """
        Append to last
        complexity: O(1)
        :param value:
        :return:
        """
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
        """
        Remove last element
        complexity: O(1)
        :return:
        """
        if self.length == 0:
            return None
        tail = self.tail
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None

        tail.prev = None
        return tail

    def prepend(self, value):
        """
        Add to initial index
        complexity: O(1)
        :param value:
        :return:
        """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.length = 1
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            self.length += 1
        return True

    def pop_first(self):
        """
        Remove first element
        complexity: O(1)
        :return:
        """
        if self.length == 0:
            return None
        head = self.head
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None

        head.next = None
        return head

    def get(self, index):
        """
        Get item by index
        complexity: O(n)
        :param index:
        :return:
        """
        if index < 0 or index >= self.length:
            return None
        if index <= self.length // 2:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            return temp
        else:
            temp = self.tail
            for _ in range(self.length - index - 1):
                temp = temp.prev
            return temp

    def set_value(self, index, value):
        """
        Set value at an index
        complexity: O(n)
        :param index:
        :param value:
        :return:
        """
        if index < 0 or index >= self.length:
            return None
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False


if __name__ == "__main__":
    ll = DoublyLinkedList(1)
