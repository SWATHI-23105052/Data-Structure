class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class DLL:

    def __init__(self):
        self.head=None
        self.temp=None
    
    def Create(self):
        num=int(input("Enter number of data:"))
        for i in range(num):
            data=int(input("Enter data: "))
            newnode=Node(data)
            if self.head is None:
                self.head=newnode
                self.temp=newnode
            else:
                self.temp.next=newnode
                newnode.prev=self.temp
                self.temp=newnode

    def Display(self):
        self.temp = self.head
        while self.temp is not None:
            print(self.temp.data, end=" ->")
            self.temp = self.temp.next
        

    def Insert_Begin(self):
        data = int(input("\nEnter data: "))
        newnode = Node(data)
        newnode.next=self.head
        self.head.prev=newnode
        self.head=newnode

    def Insert_End(self):
        data=int(input("\nEnter data: "))
        newnode=Node(data)
        self.temp=self.head
        while self.temp.next  is not None:
            self.temp=self.temp.next
        newnode.prev=self.temp
        self.temp.next=newnode
    
    def Insert_Middle(self):
        position=int(input("Enter Position: "))
        data=int(input("\nEnter data: "))
        newnode=Node(data)
        self.temp=self.head
        # for i in range(position-1):
        #     previous=self.temp
        #     self.temp=self.temp.next
        # newnode.next=self.temp
        # newnode.prev=previous
        # self.temp.prev=newnode
        # previous.next=newnode
                # "OR"

        for i in range(position-1):
            self.temp=self.temp.next
        newnode.next=self.temp
        newnode.prev=self.temp.prev
        self.temp.prev.next=newnode
        self.temp.prev=newnode
        

    
    def Delete_Begin(self):
        self.temp=self.head
        self.head=self.head.next
        self.head.prev=None
        del(self.temp)

#del at end and del at beginning
        
    def Delete_End(self):
        self.temp=self.head
        while self.temp.next is not None:
            self.temp=self.temp.next
        temp=self.temp
        self.temp.prev.next=None
        del(temp)
    
    def Delete_Middle(self):
        self.temp=self.head
        position=int(input())
        for i in range(position-1):
            self.temp=self.temp.next
        


        

d1=DLL()
d1.Create()
d1.Display()
print()
d1.Delete_Begin()
d1.Display()
print()
# d1.Insert_Begin()
# d1.Display()
# print()
# d1.Insert_End()
# d1.Display()
# print() 
d1.Insert_Middle()
d1.Display()