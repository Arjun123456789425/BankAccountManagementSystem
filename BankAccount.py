from abc import ABC , abstractmethod

#Creating a class
class BankAccount(ABC):
    def __init__(self,balance):
        self.__balance =balance

    @property
    def balance(self):
        return self.__balance

    def deposit(self, i_amount):
        try:

            if i_amount <= 0:
                raise ValueError('Deposit amount must be positive')

            self.__balance += i_amount
            print('Deposited:', i_amount)

        except (ValueError, TypeError) as e:
            print('the entered amount must be number')

    def withdraw(self, i_amount):
        try:

          if i_amount <= 0:
            raise ValueError("Amount must be positive")

          if i_amount > self.__balance:
            raise ValueError("Insufficient balance")

          self.__balance -= i_amount

          print("Withdrawn amount:", i_amount)
          print("Balance amount:", self.__balance)

        except (ValueError ,TypeError)  as e:
            print('The entered amount must be a number')

#This abstract method must be inherited by the child classes
    @abstractmethod
    def calculate_interest():
        pass

    def display_balance(self):  
        print('the account balance:',self.__balance)

    

     