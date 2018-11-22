# The first exercise of Object Oriented Programming. Create a bank account.
# Make it possible to deposit money into it and to withdraw money from it.


class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0.0

    def deposit(self, money_to_add):
        m = money_to_add
        o = self.owner
        print("\nDeposited {} to {}'s account".format(m, o))
        self.balance += money_to_add
        return self.balance

    def withdraw(self, money_to_take):
        if money_to_take <= self.balance:
            self.balance -= money_to_take
            m = money_to_take
            o = self.owner
            print("\nWithdrew {} from {}'s account".format(m, o))
        else:
            m = money_to_take
            b = self.balance
            print("\nUnable to withdraw {} from the balance of {}.".format(m, b))
        return self.balance

    def display(self):
        print("")
        print("Owner: {}".format(self.owner))
        print("Balance: {}".format(self.balance))
        return


# Testing
account1 = BankAccount("Jari Mutikainen")
account2 = BankAccount("Karthika")
account1.display()
account1.deposit(250.0)
account1.display()
account1.withdraw(14.0)
account1.display()
account2.deposit(100.0)
account2.display()
account2.withdraw(114.0)
account2.display()
