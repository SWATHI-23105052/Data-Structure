class Balancing_Paranthesis():
    def __init__(self,size):
        self.stack=[]
        self.size=size


    def is_balanced(self,exp):
        for char in exp:
            if char in '{[(':
                self.push(char)

            elif char in '}])':
                if not self.stack:
                    print("Right paranthesis is more than left")
                    return False
                else:
                    temp=self.pop()
                    if not self.match(temp,char):
                        print("Paranthesis mismatched",temp,char)
                        return False
        if not self.stack:
            print("left paranthesis is more than right")
            return False
        return True

    def push(self,char):
        if len(self.stack)==self.size:
            print("Overflow")
        else:
            self.stack.append(char)
        
    def pop(self):
        if not self.stack:
            print("Underflow")
        else:
            return self.stack.pop()
        
        

    def match(self,temp,char):
        if (temp=='{' and char=='}'):
            return True
        elif (temp=='(' and char==')'):
            return True
        elif (temp=='[' and char==']'):
            return True
        else:
            return False
        


if __name__ =="__main__":
    size=int(input("Enter size of stack: "))
    exp=input("Enter the expression: ")
    bp=Balancing_Paranthesis(size)
    result=bp.is_balanced(exp)
    if result:
        print("Balanced")
    else:
        print("Unbalanced")
