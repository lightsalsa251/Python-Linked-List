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
    def swapper(self,x,y):
        ptr = self.head
        pre_ptr = None
        ptr1 = self.head
        pre_ptr1 = None
        while ptr != None and ptr.data!=x:
            pre_ptr = ptr
            ptr = ptr.next
        #print(pre_ptr.data,'    ',ptr.data)
        while ptr1!=None and ptr1.data!=y:
            pre_ptr1 = ptr1
            ptr1 = ptr1.next
        #print(ptr1.data)
        pre_ptr.next = ptr1
        pre_ptr1.next = ptr
        temp = ptr.next
        ptr.next = ptr1.next
        ptr1.next = temp
if __name__=='__main__':
    llist = LinkedList()
    llist.add_first(60)
    llist.add_first(50)
    llist.add_first(40)
    llist.add_first(30)
    llist.add_first(20)
    llist.add_first(10)
    llist.swapper(20,50)
    llist.printList()
