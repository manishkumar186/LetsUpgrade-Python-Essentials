class bank_account:
    ownerName="manish"
    Balance =1000
    def deposit(self,add):
        self.Balance= self.Balance+add
        print("Amount is credit ",add)
        print("Total balance is: ",self.Balance)

    def withdraw(self,debit):
        if(self.Balance>=debit):
            self.Balance = self.Balance-debit
            print("Amount is debited ",debit)
            print("Total balance is: ",self.Balance)
        else:
            print("No sufficent balance ")

obj = bank_account()
obj.deposit(1000)
obj.withdraw(500)

obj1 = bank_account()
obj1.deposit(2000)
obj1.withdraw(3001)