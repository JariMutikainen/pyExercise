# The first exercise of Object Oriented Programming. Create a bank account.
# Make it possible to deposit money into it and to withdraw money from it.

class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0.0

    def deposit(self,money_to_add):
        self.balance += money_to_add
        return self.balance

    def withdraw(self,money_to_take):
        if money_to_take <= self.balance:
            self.balance -= money_to_take
        else:
            print("Unable to withdraw{} ".format(money_to_take))
            print("from the balance of {}.".format(self.balance))
        return self.balance
    
    def display(self):
        print("")
        print("Owner: {}".format(self.owner))
        print("Balance: {}".format(self.balance))
        return

# Testing
account1 = BankAccount("Jari Mutikainen")
account1.display()
account1.deposit(250.0)
account1.display()
account1.withdraw(14.0)
account1.display()

