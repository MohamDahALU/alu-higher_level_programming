#!/usr/bin/python3


class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @property
    def next_node(self):
        return self.__next_node

    @data.setter
    def data(self, value):
        if type(value) != int:
            raise TypeError("data must be an integer")
        self.__data = value

    @next_node.setter
    def next_node(self, value):
        if isinstance(value, (Node, type(None))):
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    def __init__(self):
        self.__head = None

    def __str__(self):
        node_list = ""
        head = self.__head
        while head:
            node_list += f"{str(head.data)}"
            if head.next_node:
                node_list += "\n"
            head = head.next_node

        return node_list

    def sorted_insert(self, value):

        new_node = Node(value, self.__head)

        if not self.__head:
            self.__head = new_node
            return 0

        if not self.__head.next_node:
            if new_node.data <= self.__head.data:
                self.__head = new_node
            else:
                new_node.next_node = None
                self.__head.next_node = new_node
            return 0
        else:
            if new_node.data <= self.__head.data:
                self.__head = new_node
                return 0

        head = self.__head
        while True:
            if not head.next_node:
                head.next_node = new_node
                new_node.next_node = None
                return 0

            if new_node.data <= head.next_node.data:
                new_node.next_node = head.next_node
                head.next_node = new_node
                return 0

            head = head.next_node


sll = SinglyLinkedList()
sll.sorted_insert(2)
sll.sorted_insert(5)
sll.sorted_insert(3)
sll.sorted_insert(10)
sll.sorted_insert(1)
sll.sorted_insert(-4)
sll.sorted_insert(-3)
sll.sorted_insert(4)
sll.sorted_insert(5)
sll.sorted_insert(12)
sll.sorted_insert(3)
print(sll)
