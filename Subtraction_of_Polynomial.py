class Node:
    def __init__(self,coeff,exp):
        self.coeff = coeff
        self.exp = exp
        self.next=None

class Polynomial:
    def __init__(self):
        self.head=None
        self.temp=None
    
    def Create(self,coeff,exp):
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


def Subtraction_Of_Polynomial(p1,p2):
    l1=p1.head
    l2=p2.head
    p3=Polynomial()
    while l1 and l2:
        if l1.exp==l2.exp:
            p3.Create(l1.coeff-l2.coeff,l1.exp)
            l1=l1.next
            l2=l2.next
        elif l1.exp>l2.exp:
            p3.Create(l1.coeff,l1.exp)
            l1=l1.next
        else:
            p3.Create(-l2.coeff,l2.exp)
            l2=l2.next
    while l1:
        p3.Create(l1.coeff,l1.exp)
        l1=l1.next
    while l2:
        p3.Create(-l2.coeff,l2.exp)
        l2=l2.next


    p3.Display()
p1=Polynomial()
n=int(input("Enter number of terms: "))
for i in range(n):
    coeff=int(input("Enter the Coefficient: "))
    exp=int(input("Enter the Exponent : "))
    p1.Create(coeff,exp)
    
p2=Polynomial()
n=int(input("Enter number of terms: "))
for i in range(n):
    coeff=int(input("Enter the Coefficient: "))
    exp=int(input("Enter the Exponent : "))
    p2.Create(coeff,exp)


Subtraction_Of_Polynomial(p1,p2)