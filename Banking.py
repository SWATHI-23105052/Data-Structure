class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        return amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return amount
        else:
            return "Insufficient balance"

    def display(self):
        return self.balance

account = BankAccount()
accno=int(input("Enter Account Number:"))
name=input("Enter your Name:")
a=int(input("Enter the amount deposited:"))
b=int(input("Enter the amount of withdrawal:"))
print("Account Number:",accno)
print("Account holder Name:",name)
print("Amount Deposited: $",account.deposit(a))
print("You Withdrew: $",account.withdraw(b))
print("Net Available Balance: $",account.display())