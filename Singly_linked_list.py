class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SLL:
    def __init__(self):
        self.head = None
        self.temp = None
    
    def Create(self):
        num = int(input("Enter number of nodes: "))
        for i in range(num):
            data = int(input("Enter data: "))
            newnode = Node(data)
            if self.head is None: 
                self.head = newnode
                self.temp = newnode
            else:
                self.temp.next = newnode  
                self.temp = newnode       
        
    def Display(self):
        self.temp = self.head
        while self.temp is not None:
            print(self.temp.data, end=" ->")
            self.temp = self.temp.next


    # def Insert_Begin(self):
    #     data = int(input("\nEnter data: "))
    #     newnode = Node(data)
    #     newnode.next=self.head
    #     self.head=newnode


    # def Insert_End(self):
    #     data = int(input("\nEnter data: "))
    #     newnode = Node(data)
    #     self.temp=self.head
    #     while self.temp.next is not None:
    #         self.temp = self.temp.next
    #     self.temp.next = newnode

    # def Insert_Middle(self):
    #     data = int(input("\nEnter data: "))
    #     newnode = Node(data)
    #     n=int(input("Enter the position: "))
    #     self.temp=self.head
    #     for i in range(n-1):
    #         prev=self.temp
    #         self.temp=self.temp.next
    #     newnode.next=self.temp
    #     prev.next=newnode

    def Delete_start(self):
        temp=self.head
        self.head=self.head.next
        del(temp)
    
    def Delete_End(self):
        self.temp=self.head
        prev=self.temp
        while self.temp.next is not None:
            prev=self.temp
            self.temp=self.temp.next
        prev.next=None
        del(self.temp)

    def Delete_Middle(self):
        n=int(input("Enter the position: "))
        self.temp=self.head
        for i in range(n-1):
            prev=self.temp
            self.temp=self.temp.next
        prev.next=self.temp.next
        del(self.temp)

    def Count(self):
        self.temp = self.head
        count=0
        while self.temp is not None:
            count+=1
            self.temp = self.temp.next
        print(count)
    

        

s1 = SLL()
s1.Create()
s1.Display()
print()
s1.Count()
# s1.Insert_Begin()
# s1.Display()

# s1.Insert_End()
# s1.Display()
# s1.Insert_Middle()
# s1.Display()

s1.Delete_start()
print()
s1.Display()

# s1.Delete_End()
# print()
# s1.Display()