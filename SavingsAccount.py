from BankAccount import BankAccount

class SavingsAccount(BankAccount):
    def __init__(self, balance =0):
        super().__init__(balance)
        print("Interest:", self.calculate_interest())
        
    def calculate_interest(self):
        intrest = self.balance   *0.05
        return intrest




    