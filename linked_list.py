import copy


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
        self.head.next = self.tail
        self.length = 1

    def print_list(self):
        """
        Print all items in linked list.
        Iterate though all nodes starting from head,
        till the next node is None
        :return:
        """
        temp = self.head

        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        """
        Append new item

        complexity: O(1)

        :param value:
        :return:
        """

        # Check if list is empty,
        # if yes create and assign
        # a new node as head and tail,
        # else set next of tail as new node,
        # reassign new node as
        # new tail and increment length.
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.length = 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
        return True

    def pop(self):
        """
        Pop the tail(last item)

        Here we have to remove the tail as well as
         re-index the List

         complexity: O(n)
        :return:
        """
        # Check if length is zero, return None
        if self.length == 0:
            return None
        # Here we have to remove and return the tail
        # Iterate till the node before tail
        tail = self.tail
        temp = self.head
        new_tail = temp
        while temp.next:
            new_tail = temp
            temp = temp.next
        # Assign the second last node as tail and
        # its next asn None
        new_tail.next = None
        self.tail = new_tail
        # Decrement length and see if its 0.
        # If yes, set head and tail as None
        # Finally return the initial tail
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return tail

    def prepend(self, value):
        """
        Add item to beginning
         complexity: O(1)
        :param value:
        :return:
        """

        # Create a new Node and check if length is zero.
        # If yes assign new Node as head and tail
        # else set new node's next as the list's head and
        # set new node as the new head.
        # Finally, increment length.
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

        complexity: O(1)
        :return:
        """

        # If length is zero return None
        if self.length == 0:
            return None
        # Get the head and set new head as next of initial head
        first = self.head
        new_head = first.next
        self.head = new_head
        # Clear the next of this head
        first.next = None
        # Decrement length, if length is zero, set tail as None
        # Finally, return the first element.
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return first

    def get(self, index):
        """
        Get node by index

        complexity: O(n)
        :param index:
        :return:
        """
        # Check if index is valid, else return None
        if index < 0 or index >= self.length:
            return None
        # Start from head and iterate through
        # next nodes till we get to index
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, value):
        """
        Set value of a node by index
        complexity: O(n)
        :param index:
        :param value:
        :return:
        """

        # Get the node corresponding to index
        # Update the value
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False


if __name__ == "__main__":
    ll = LinkedList(1)
    ll.print_list()
