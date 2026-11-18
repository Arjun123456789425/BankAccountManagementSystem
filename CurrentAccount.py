from BankAccount import BankAccount
#INHERITANCE - We  inherit methods and properties of parent class
class CurrentAccount(BankAccount):
  def __init__(self, balance = 0):
    super().__init__(balance)
  


  def calculate_interest(self):
     intrest = 0
     return intrest 