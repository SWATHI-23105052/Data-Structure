class Node:
    def __init__(self,coeff,exp):
        self.coeff = coeff
        self.exp = exp
        self.next=None

class Polynomial:
    def __init__(self):
        self.head=None
        self.temp=None
    
    def Create(self):
        n=int(input("Enter number of terms: "))
        for i in range(n):
            coeff=int(input("Enter the Coefficient: "))
            exp=int(input("Enter the Exponent : "))
            newnode=Node(coeff,exp)
            if self.head is None or self.head.exp < newnode.exp:
                newnode.next=self.head
                self.head=newnode
            else:
                self.temp=self.head
                while self.temp.next is not None and newnode.exp < self.temp.next.exp:
                    self.temp=self.temp.next
                newnode.next=self.temp.next
                self.temp.next=newnode

    def Display(self):
        self.temp = self.head
        while self.temp is not None:
            print(f"{self.temp.coeff}x^{self.temp.exp}", end=" + " if self.temp.next is not None else "")
            self.temp = self.temp.next

p1=Polynomial()
p1.Create()
p1.Display()