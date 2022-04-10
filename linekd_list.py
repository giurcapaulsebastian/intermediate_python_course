class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head:
            current = self.head
            print(current.data, end=" ")
            while current.next:
                current = current.next
                print(current.data, end=" ")
        else:
            print("Empty list!")

    #insert, insert after

    def insert_first(self, data):
        to_insert = Node(data)
        if self.head is None:
            self.head = to_insert
        else:
            next = self.head
            self.head = to_insert
            to_insert.next = next
    


def run():
    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)

    llist.head.next = second
    second.next = third
    llist.print()

run()