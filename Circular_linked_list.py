class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CLL:
    def __init__(self):
        self.head = None
        self.temp = None
        self.tail=None
    
    def Create(self):
        num = int(input("Enter number of nodes: "))
        for i in range(num):
            data = int(input("Enter data: "))
            newnode = Node(data)
            if self.head is None: 
                self.head = newnode
                self.temp = newnode
                self.tail=newnode
            else:
                self.temp.next = newnode  
                self.temp = newnode
                self.tail=newnode
                self.tail.next=self.head
    
    def Display(self):
        self.temp = self.head
        while self.temp.next is not self.head:
            print(self.temp.data, end=" ->")
            self.temp = self.temp.next
        print(self.temp.data)


    def Insert_Begin(self):
        data = int(input("\nEnter data: "))
        newnode = Node(data)
        newnode.next=self.head
        self.head=newnode
        self.tail.next=self.head

    def Insert_End(self):
        data = int(input("\nEnter data: "))
        newnode = Node(data)
        self.temp=self.head
        newnode.next=self.head
        self.tail.next=newnode
        self.tail=newnode
    
    def Insert_Middle(self):
        data=int(input("Enter the data:"))
        position=int(input("Enter the position:"))
        newnode=Node(data)
        self.temp=self.head
        for i in range(position-1):
            prev=self.temp
            self.temp=self.temp.next
        newnode.next=self.temp
        prev.next=newnode
        

    def Delete_start(self):
        self.temp=self.head
        self.head=self.head.next
        self.tail.next=self.head
        del(self.temp)
        

    def Delete_End(self):
        self.temp=self.head
        while self.temp.next is not self.head:
            prev=self.temp
            self.temp=self.temp.next
        prev.next=self.head
        del(self.temp)
        

    def Delete_Middle(self):
        n=int(input("enter the position:"))
        self.temp=self.head
        for i in range(n-1):
            prev=self.temp
            self.temp=self.temp.next
        prev.next=self.temp.next
        del(self.temp)

    def Count(self):
        self.temp=self.head
        count = 0
        while self.temp.next is not self.head:
            count += 1
            self.temp = self.temp.next
        print(count)
    
    def Search_Element(self):
        search=int(input("Enter Search element:"))
        self.temp=self.head
        flag=0
        while self.temp.next is not self.head:
            if(self.temp.data is search):
                print("Element Found")
                flag=1
                break
            self.temp=self.temp.next
        if(self.tail.data==search):     #checking last element alone
            print("Element found")
            flag=1
        if(flag==0):
            print("Element not found")
        
        

        
    

    

s1=CLL()
s1.Create()
s1.Display()
s1.Insert_Begin()
s1.Display()
s1.Insert_End()
s1.Display()
s1.Insert_Middle()
s1.Display()
s1.Delete_start()
s1.Display()
s1.Delete_Middle()
s1.Display()
s1.Delete_End()
s1.Display()
s1.Count()
s1.Display()
s1.Search_Element()
