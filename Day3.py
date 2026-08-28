'''# Doubly Linked List
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
class DoublyLinkedList:
    def __init__(self):
        self.head = None
    def display(self):
        temp = self.head
        while temp:
            print(temp.value, end=" <-> ")
            temp = temp.next
        print("None")
    def delete(self, value):
        temp = self.head
        while temp:
            if temp.value == value:
                if temp.prev:
                    temp.prev.next = temp.next
                if temp.next:
                    temp.next.prev = temp.prev
                if temp == self.head:
                    self.head = temp.next
                return
            temp = temp.next
    def pop(self):
        temp = self.head
        if temp is None:
            return
        while temp.next:
            temp = temp.next
        if temp.prev:
            temp.prev.next = None
        else:
            self.head = None
# Create list
dll = DoublyLinkedList()
dll.head = Node(10)
dll.head.next = Node(20)
dll.head.next.prev = dll.head
dll.head.next.next = Node(30)
dll.head.next.next.prev = dll.head.next
dll.display()
dll.delete(20)
dll.display()
dll.pop()
dll.display()


'''
# Circular Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    # Add node at the end
    def add(self, data):
        new = Node(data)

        if self.head is None:
            self.head = new
            new.next = self.head
            return

        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        temp.next = new
        new.next = self.head

    # Remove a specific value
    def remove(self, data):
        if self.head is None:
            return None

        # Remove head
        if self.head.data == data:

            # Only one node
            if self.head.next == self.head:
                self.head = None
                return data

            temp = self.head

            while temp.next != self.head:
                temp = temp.next

            self.head = self.head.next
            temp.next = self.head

            return data

        # Remove middle/last node
        temp = self.head

        while temp.next != self.head:
            if temp.next.data == data:
                value = temp.next.data
                temp.next = temp.next.next
                return value

            temp = temp.next

        return None

    # Remove last node and return its value
    def pop(self):
        if self.head is None:
            return None

        # Only one node
        if self.head.next == self.head:
            value = self.head.data
            self.head = None
            return value

        temp = self.head

        while temp.next.next != self.head:
            temp = temp.next

        value = temp.next.data
        temp.next = self.head

        return value

    # Display list
    def display(self):
        if self.head is None:
            print("Empty")
            return

        temp = self.head

        while True:
            print(temp.data, end=" -> ")
            temp = temp.next

            if temp == self.head:
                break

        print("Head")
c = CircularLinkedList()

c.add(10)
c.add(20)
c.add(30)
c.add(40)

c.display()

print("Removed:", c.remove(20))
c.display()

print("Popped:", c.pop())
c.display()
