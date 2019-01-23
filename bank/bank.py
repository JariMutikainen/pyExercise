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

    def creation(self):
        owner = input('Enter your name: ')
        initial_depo = input('Enter your initial deposit amount: ')
        account_number = randint(1,100000)
        while account_number in self.accounts.keys():
            # Keep generating 5-digit random numbers until you find an
            # unused one.
            account_number = randint(1,100000)
        self.accounts[account_number] = Account(owner, initial_depo)
        print(f'\nHello {owner}\n'
              f'The account number of your new savings account is '
              f'{account_number:0>5d}\n'
              f'The initial balance of that account was set to {initial_depo}')

    def deposition(self):
        print('deposition')

    def withdrawal(self):
        print('withdrawal')

    def query(self):
        print('query')

    def exition(self):
        print('Thank you for using our banking system.')
        exit(0)

    def run_bank(self):
        actions = {'1': self.creation,
                   '2': self.deposition,
                   '3': self.withdrawal,
                   '4': self.query,
                   '5': self.exition}

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
