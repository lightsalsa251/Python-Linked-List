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
    def add_at_k(self,prev,data):
        if prev is None:
            print('Previous node not available')
        new_node = Node(data)
        new_node.next = prev.next
        prev.next = new_node
    def add_last(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        ptr = self.head
        while ptr.next:
            ptr = ptr.next
        ptr.next = new_node
        new_node.next = None
    def del_first(self):
        ptr = self.head
        self.head = ptr.next
    def del_last(self):
        ptr = self.head
        while ptr.next.next:
            ptr = ptr.next
        ptr.next = None
    def del_key(self,key):
        ptr = self.head
        prev = self.head
        if ptr.data == key:
            llist.del_first()
        
        #print('Remaining are :')
        while ptr:
            if ptr.data==key:
                break
            prev = ptr
            ptr = ptr.next
        if ptr==None:
            return
        prev.next = ptr.next
        ptr = None
    def del_pos(self,pos):
        ptr = self.head
        if pos==0:
            llist.del_first()
        for i in range(pos-1):
            ptr = ptr.next
            if ptr is None:
                break
        next1 = ptr.next.next
        ptr.next = None
        ptr.next = next1
 
# Code execution starts here
if __name__=='__main__':
 
    # Start with the empty list
    llist = LinkedList()
    llist.add_first(2)
    llist.add_first(23)
    llist.add_at_k(llist.head,44)
    llist.add_last(12)
    llist.printList()
    llist.del_first()
    llist.del_last()
    llist.printList()
    print('Remaining are :')
    llist.del_key(2)
    #print('Remaining are :')
    llist.printList()
    llist.add_first(21)
    llist.add_first(26)
    llist.add_first(25)
    llist.add_first(24)
    llist.printList()
    print('After deleting')
    llist.del_pos(2)
    llist.printList()
