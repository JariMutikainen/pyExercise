# Simulate a banking system in which the user can:
#
# 1. Open a new savings account with an initial deposit
# 2. Withdraw money from his existing savings account
# 3. Deposit money into his savings account
# 4. Show the current balance of his account
#
# Use the random number generator for creating 5-digit account numbers when
# creating a new account. To access a given account the user must provide
# the correct account number and the correct name of the account owner.

from random import randint
from account import Account
from sys import exit
            
            
class Bank:

    def __init__(self):
        self.accounts = {}

    @staticmethod
    def get_details():
        owner = input('Enter your name: ')
        acc_num = input('Enter your 5-digit account number: ')
        return (owner, acc_num)

    def creation(self):
        owner = input('Enter your name: ')
        initial_depo = input('Enter your initial deposit amount: ')
        account_number = randint(1,100000)
        while account_number in self.accounts.keys():
            # Keep generating 5-digit random numbers until you find an
            # unused one.
            account_number = randint(1,100000)
        acc_num = f'{account_number:0>5d}'
        self.accounts[acc_num] = Account(owner, acc_num, initial_depo)

    def deposit(self):
        owner, acc_num = self.get_details()
        depo_amount = input('Enter amount to be deposited: ')
        self.accounts[acc_num].deposit(owner, acc_num, depo_amount)

    def withdraw(self):
        owner, acc_num = self.get_details()
        wd_amount = input('Enter amount to be withdrawn: ')
        self.accounts[acc_num].withdraw(owner, acc_num, wd_amount)

    def query(self):
        owner, acc_num = self.get_details()
        try:
            self.accounts[acc_num].show_balance(owner, acc_num)
        except KeyError:
            print(f'\n\tAccount number {acc_num} does not exist.')

    def exit_(self):
        print('\n\tThank you for using our banking system.')
        exit(0)

    def run_bank(self):
        actions = {'1': self.creation,
                   '2': self.deposit,
                   '3': self.withdraw,
                   '4': self.query,
                   '5': self.exit_}

        while True:
            print('\nCreate new savings account:          1\n'
                  'Deposit money into the account:      2\n'
                  'Withdraw money from the account:     3\n'
                  'Show current balance of the account: 4\n'
                  'Exit banking system:                 5\n')
            choice = input('Select action: ')
            try:
                actions[choice]()
            except KeyError:
                print('\nIllegal input. try again.')


if __name__ == '__main__':
    bank = Bank()
    bank.run_bank()
