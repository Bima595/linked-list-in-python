class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None   

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node


    def sort_list(self):
        curr_node = self.head
        while curr_node:
            min_node = curr_node
            next_node = curr_node.next
            while next_node:
                if next_node.data < min_node.data:
                    min_node = next_node
                next_node = next_node.next
            if curr_node != min_node:
                curr_node.data, min_node.data = min_node.data, curr_node.data
            curr_node = curr_node.next

    def print_list(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.data)
            curr_node = curr_node.next



linked_list = LinkedList()


linked_list.append("7")
linked_list.append("1")
linked_list.append("4")
linked_list.append("6")
linked_list.append("2")
linked_list.append("3")


print("Before")
linked_list.print_list()  
print("After")
linked_list.sort_list()

linked_list.print_list() 

