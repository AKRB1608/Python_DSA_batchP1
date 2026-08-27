'''arr=[1,2,3,4]
print(hex(id(arr[0])))  
print(hex(id(arr[1]))) 
print(hex(id(arr[2])))
print(hex(id(arr[3]))) 
'''''
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

node1.next = node2
node2.next = node3


def display(head):
    current = head

    while current:
        print(current.value, end=" -> ")
        current = current.next

    print("None")


def insert_beginning(head, value):
    new_node = Node(value)
    new_node.next = head
    return new_node


def insert_end(head, value):
    new_node = Node(value)

    if head is None:
        return new_node

    current = head

    while current.next:
        current = current.next

    current.next = new_node
    return head


def search(head, value):
    current = head

    while current:
        if current.value == value:
            return True
        current = current.next

    return False


def delete(head, value):
    if head is None:
        return None

    if head.value == value:
        return head.next

    current = head

    while current.next:
        if current.next.value == value:
            current.next = current.next.next
            return head

        current = current.next

    return head


def update(head, old_value, new_value):
    current = head

    while current:
        if current.value == old_value:
            current.value = new_value
            return head

        current = current.next

    return head


head = node1

display(head)

head = insert_beginning(head, 5)
display(head)

head = insert_end(head, 40)
display(head)

print(search(head, 30))

head = update(head, 20, 25)
display(head)

head = delete(head, 30)
display(head)

head = delete(head, 5)
display(head)