class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None
class SinglyLinkedList:
    def __init__(self):
        self.first=None
    def insertFirst(self,data):
        temp=Node(data)
        if(self.first==None):
            self.first=temp
        else:
            temp.next=self.first
            self.first=temp
    def removeFirst(self):
        if(self.first==None):
            print("list is empty")
        else:
            cur=self.first
            self.first=self.first.next
            print("the deleted item is",cur.data)
    def display(self):
       if(self.first==None):
           print("list is empty")
           return
       current=self.first
       while(current):
           print(current.data,end=" ")
           current=current.next
    def search(self,item):
       if(self.first==None):
           print("list is empty")
           return
       current=self.first
       found=False
       while current !=None and not found:
           if current.data==item:
               found=True
           else:
               current=current.next
           if(found):
               print("Item is present in the linked list")
           else:
               print("Item is not present in the linked list")
#Singly Linked List
ll=SinglyLinkedList()
while(True):
    c1=int(input("\nEnter your choice 1-insert 2-delete 3-search 4-display 5-exit"))
    if(c1==1):
        item=input("Enter the elements to insert:")
        ll.insertFirst(item)
        ll.display()
    elif(c1==2):
        ll.removeFirst()
        ll.display()
    elif(c1==3):
        item=input("Enter the element to search:")
        ll.search(item)
    elif(c1==4):
        ll.display()
    else:
        break