class BankAccount :
    def __init__(self) :
        self.accno = 210033
        self.name = "Hamras"
        self.acctype = "savings"
        self.balance = 0
    def deposit(self) :
        amount = int(input("Enter the amount to be deposited : "))
        self.balance = self.balance + amount
        print("Amount deposited successfully")
    def withdraw(self) :
        amount = int(input("Enter the amount to withdraw : "))
        if (self.balance<amount) :
            print("Insufficient Balance")
        else :
            self.balance = self.balance - amount
            print("Amount withdrawn successfully")
    def display(self) :
        print("Account Number : ",self.accno," Account Holder Name : ",self.name,"Account type : ",self.acctype,
        " Current Balance : ",self.balance)
ob = BankAccount()
ob.deposit()
ob.withdraw()
ob.display()