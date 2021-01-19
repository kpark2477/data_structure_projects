class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = "-> "
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):

    node1 = llist_1.head
    node2 = llist_2.head
    
    if node1 == None:
        return llist_2
    if node2 == None:
        return llist_1

    output = set()
    def add(node1, node2):
        if node1.value == node2.value:
            return
        else:
            if node2.next:
                add(node1, node2.next)
            else:
                output.add(node1.value)
    def add2(node1, node2):
        add(node1, node2)
        if node1.next:
            add2(node1.next, node2)
    add2(node1, node2)
    add2(node2, node1)

    output_linkedlist = LinkedList()

    for i in output:
        output_linkedlist.append(i)

    intersection_linkedlist = intersection(llist_1, llist_2)
    
    output_node = output_linkedlist.head
    while output_node.next:
        output_node = output_node.next

    output_node.next = intersection_linkedlist.head

    return output_linkedlist

def intersection(llist_1, llist_2):
    # Your Solution Here
    node1 = llist_1.head
    node2 = llist_2.head
    if node1 == None or node2 == None:
        return LinkedList()

    output = set()
    def add(node1, node2):
        if node1.value == node2.value:
            output.add(node1.value)
        else:
            if node2.next:
                add(node1, node2.next)
    def add2(node1, node2):
        add(node1, node2)
        if node1.next:
            add2(node1.next, node2)
    add2(node1, node2)

    output_linkedlist = LinkedList()

    for i in output:
        output_linkedlist.append(i)

    return output_linkedlist


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))

# Test case 3

linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = []
element_2 = []

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print (union(linked_list_5,linked_list_6))
print (intersection(linked_list_5,linked_list_6))

# Test case 4

linked_list_7 = LinkedList()
linked_list_8 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = []

for i in element_1:
    linked_list_7.append(i)

for i in element_2:
    linked_list_8.append(i)

print (union(linked_list_7,linked_list_8))
print (intersection(linked_list_7,linked_list_8))