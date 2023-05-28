class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
 
class DoublyLinkedList:
 
    def __init__(self):
        self.head = None
 
    def merge(self, first, second):
        if first is None:
            return second
        if second is None:
            return first
 
        if first.data < second.data:
            first.next = self.merge(first.next, second)
            first.next.prev = first
            first.prev = None  
            return first
        else:
            second.next = self.merge(first, second.next)
            second.next.prev = second
            second.prev = None
            return second
 
    def mergeSort(self, tempHead):
        if tempHead is None:
            return tempHead
        if tempHead.next is None:
            return tempHead
         
        second = self.split(tempHead)
        tempHead = self.mergeSort(tempHead)
        second = self.mergeSort(second)
        return self.merge(tempHead, second)

    def split(self, tempHead):
        fast = slow =  tempHead
        while(True):
            if fast.next is None:
                break
            if fast.next.next is None:
                break
            fast = fast.next.next
            slow = slow.next
             
        temp = slow.next
        slow.next = None
        return temp

    def push(self, new_data):
  
        new_node = Node(new_data)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node
 
 
    def printList(self, node):
        temp = node
        while(node is not None):
            print (node.data,end=" ")
            temp = node
            node = node.next


dll = DoublyLinkedList()
n=int(input("Enter how many data?"))

for i in range(n):
    s=int(input("Enter data"))
    dll.push(s)
dll.head = dll.mergeSort(dll.head)  
dll.printList(dll.head)