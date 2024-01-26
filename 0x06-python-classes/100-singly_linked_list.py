#!/usr/bin/python3
"""Defines the classes for a singly-linked list."""


class Node:
    """This represents a node in a singly-linked list."""

    def __init__(self, data, next_node=None):
        """Initialize a new Node.
        Args:
            data (int): The data of the new Node.
            next_node (Node): The next node."""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """It gets the data of the Node."""
        return (self.__data)

    @data.setter
    def data(self, value):
        """It gets the data of the Node."""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """This gets the next_node."""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """It sets the next_node."""
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """This represents a singly-linked list."""

    def __init__(self):
        """It initalizes a new SinglyLinkedList."""
        self.__head = None

    def sorted_insert(self, value):
        """This adds a new Node into the SinglyLinkedList.
        Args:
            value (Node): Node to insert."""
        new_node = Node(value)
        if self.__head is None:
            new_node.next_node = None
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            temp = self.__head
            while (temp.next_node is not None and
                    temp.next_node.data < value):
                temp = temp.next_node
            new_node.next_node = temp.next_node
            temp.next_node = new_node

    def __str__(self):
        """This defines the eqivalent of print() of a SinglyLinkedList."""
        values = []
        temp = self.__head
        while temp is not None:
            values.append(str(temp.data))
            temp = temp.next_node
        return ('\n'.join(values))
