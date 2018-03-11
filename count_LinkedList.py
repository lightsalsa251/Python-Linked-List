class Node:
 
    # Function to initialise the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null
 
 
# Linked List class contains a Node object
class LinkedList:
 
    # Function to initialize head
    def __init__(self):
        self.head = None
 
    # This function prints contents of linked list
    # starting from head
    def printList(self):
        temp = self.head
        while (temp):
            print (temp.data)
            temp = temp.next
    def add_first(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def count_iter(self):
        ptr = self.head
        count = 0
        while ptr:
            count+=1
            ptr = ptr.next
        print('length is ',count)
    def count_recursive(self,ptr):
        if not ptr:
            return 0
        else:
            return 1 + self.count_recursive(ptr.next) 
if __name__=='__main__':
    llist = LinkedList()
    llist.add_first(20)
    llist.add_first(30)
    llist.add_first(40)
    llist.count_iter()
    ptr = llist.head
    a = llist.count_recursive(ptr)
    print(a)
