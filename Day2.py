'''arr=[1,2,3,4]
print(hex(id(arr[0])))  
print(hex(id(arr[1]))) 
print(hex(id(arr[2])))
print(hex(id(arr[3]))) 
'''''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new = Node(data)

        if self.head is None:
            self.head = new
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    def delete(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        temp = self.head
        while temp.next:
            if temp.next.data == data:
                temp.next = temp.next.next
                return
            temp = temp.next

    def pop(self):
        if self.head is None:
            return

        if self.head.next is None:
            self.head = None
            return

        temp = self.head
        while temp.next.next:
            temp = temp.next

        temp.next = None


l = LinkedList()

l.insert(10)
l.insert(20)
l.insert(30)

l.display()

l.delete(20)
l.display()

l.pop()
l.display()