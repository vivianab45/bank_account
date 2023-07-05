# The BankAccount class should have a balance. 
# When a new BankAccount instance is created, if an amount is given, 
# the balance of the account should initially be set to that amount;
# otherwise, the balance should start at $0. The account should also 
# have an interest rate in decimal format. For example, a 1% interest 
# rate would be saved as 0.01. The interest rate should be provided upon 
# instantiation. (Hint: when using default values in parameters, the order 
#  of parameters matters!)

# The class should also have the following methods:

# deposit(self, amount) - increases the account balance by the given amount
# withdraw(self, amount) - decreases the account balance by the given amount 
# if there are sufficient funds; if there is not enough money,
#  print a message "Insufficient funds: Charging a $5 fee" and deduct $5
# display_account_info(self) - print to the console: eg. "Balance: $100"
# yield_interest(self) - increases the account balance by the current 
# balance * the interest rate (as long as the balance is positive)

class BankAccount:

    def __init__(self, int_rate, balance=0): 
        self.int_rate=int_rate
        self.balance=balance


    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if self.balance <amount:
            print(f"Insufficient funds: deduct $5 fee")
            self.balance-= 5
        self.balance -= amount
        return self
    def display_account_info(self):
        print (f"Balance:${self.balance}")
        return self
    def yield_interest(self):
        if self.balance>0:
            self.balance+=(self.balance*self.int_rate)
        return self
        

account1=BankAccount(0.2,300)
account2=BankAccount(0.1,500)


account1.deposit(100).deposit(100).deposit(100).withdraw(100).yield_interest().display_account_info()
account2.deposit(1000).deposit(500).withdraw(25).withdraw(25).withdraw(25).withdraw(25).yield_interest().display_account_info()