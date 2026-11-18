# from CurrentAccount import CurrentAccount
# from SimpleAccount import SimpleAccount
# #Create an object of CurrentAccount

# cal =CurrentAccount()
# cal.dummy()
# sa =SimpleAccount()
# sa.method()
#from BankAccount import BankAccount
# bank =BankAccount()
# bank.deposit_amount()
#Not possible because we cannot create an object of an abstract class
# from CurrentAccount import CurrentAccount
# ca = CurrentAccount()
# ca.dummy()     #Method is defined in the child class
# ca.deposit_amount(3000) #Method is defined in the parent class
# cannot be done because variable is protected frombeing acessed from outside 
# print('balance amount is:',ca.balance) 
# ca.display_balance()
# ca.deposit_amount(-10000)
# ca.display_balance()
from SavingsAccount import SavingsAccount
from CurrentAccount import CurrentAccount

sa = SavingsAccount()

sa.deposit(10000)
sa.display_balance()
sa.calculate_interest()




print('hello')